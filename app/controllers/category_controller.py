from fastapi import HTTPException
from app.db.database import  call_collection,district_collection


async def get_category_summary(districtId: str = None, constituencyId: str = None, categoryId: str = None):
    try:
        # Fetch district and constituency map
        district_cursor = district_collection.find({}, {"_id": 0})
        district_map = {}
        async for district in district_cursor:
            district_map[district["districtId"]] = {
                "districtName": district["name"],
                "constituencies": {
                    c["constituencyId"]: c["constituencyName"] for c in district.get("constituency", [])
                }
            }

        # Filter conditions
        match_conditions = {}
        if districtId:
            match_conditions["districtId"] = districtId
        if constituencyId:
            match_conditions["constituencyId"] = constituencyId
        if categoryId:
            match_conditions["category"] = categoryId

        # Aggregation pipeline
        pipeline = [
            {"$match": match_conditions},
            {
                "$group": {
                    "_id": {
                        "districtId": "$districtId",
                        "constituencyId": "$constituencyId",
                        "category": "$category"
                    },
                    "totalIssues": {"$sum": 1},
                    "positiveFeedbackCount": {
                        "$sum": {
                            "$cond": [{"$eq": ["$feedback", "positive"]}, 1, 0]
                        }
                    },
                    "negativeFeedbackCount": {
                        "$sum": {
                            "$cond": [{"$eq": ["$feedback", "negative"]}, 1, 0]
                        }
                    }
                }
            }
        ]

        results = await call_collection.aggregate(pipeline).to_list(length=None)

        response = {}

        for item in results:
            dist_id = item["_id"]["districtId"]
            const_id = item["_id"]["constituencyId"]
            category = item["_id"]["category"]
            total_issues = item["totalIssues"]
            positivetiveCount = item["positiveFeedbackCount"]
            negativeCount = item["negativeFeedbackCount"]

            if dist_id not in response:
                response[dist_id] = {
                    "districtId": dist_id,
                    "districtName": district_map.get(dist_id, {}).get("districtName", ""),
                    "constituencies": {}
                }

            constituency_map = response[dist_id]["constituencies"]

            if const_id not in constituency_map:
                constituency_map[const_id] = {
                    "constituencyId": const_id,
                    "constituencyName": district_map.get(dist_id, {}).get("constituencies", {}).get(const_id, ""),
                    "categories": [],
                    "totalPositivePercentage": 0,
                    "totalNegativePercentage": 0
                }

            positive_percentage = round((positivetiveCount / total_issues) * 100, 2) if total_issues else 0
            negative_percentage = round((negativeCount / total_issues) * 100, 2) if total_issues else 0

            constituency_map[const_id]["categories"].append({
                "categoryName": category,
                "totalIssues": total_issues,
                "positiveFeedbackCount": positivetiveCount,
                "negativeFeedbackCount": negativeCount,
                "positivePercentage": positive_percentage,
                "negativePercentage": negative_percentage
            })

        # Compute overall positive/negative % per constituency
        for district in response.values():
            for const in district["constituencies"].values():
                total_positive = sum(c["positiveFeedbackCount"] for c in const["categories"])
                total_negative = sum(c["negativeFeedbackCount"] for c in const["categories"])
                total_feedback = total_positive + total_negative

                const["totalPositivePercentage"] = round((total_positive / total_feedback) * 100, 2) if total_feedback else 0
                const["totalNegativePercentage"] = round((total_negative / total_feedback) * 100, 2) if total_feedback else 0

        return list(response.values())

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
