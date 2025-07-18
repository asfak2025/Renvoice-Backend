import asyncio
import httpx

API_URL = "http://127.0.0.1:8000/api/district/create"  # Adjust port if needed

tamil_nadu_districts = [
    "Ariyalur", "Chengalpattu", "Chennai", "Coimbatore", "Cuddalore",
    "Dharmapuri", "Dindigul", "Erode", "Kallakurichi", "Kanchipuram",
    "Kanniyakumari", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai",
    "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai",
    "Ramanathapuram", "Ranipet", "Salem", "Sivagangai", "Tenkasi",
    "Thanjavur", "Theni", "Thoothukudi", "Tiruchirappalli", "Tirunelveli",
    "Tirupathur", "Tiruppur", "Tiruvallur", "Tiruvannamalai", "Tiruvarur",
    "Vellore", "Viluppuram", "Virudhunagar"
]

async def create_district(session, name):
    payload = {
        "name": name
    }
    try:
        response = await session.post(API_URL, json=payload)
        if response.status_code == 200:
            print(f"✅ Created: {name}")
        else:
            print(f"❌ Failed: {name} -> {response.text}")
    except Exception as e:
        print(f"❌ Error for {name}: {e}")

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [create_district(client, name) for name in tamil_nadu_districts]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
