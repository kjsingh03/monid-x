import asyncio

from app.integrations.monid.client import MonidClient


async def main() -> None:
    client = MonidClient()

    try:
        identity = await client.whoami()

        print("\n=== MONID AUTHENTICATED ===")
        print(identity)

        print("\n=== DISCOVERING GITHUB CAPABILITIES ===")

        results = await client.discover(
            "GitHub repository information",
            limit=5,
        )

        for result in results.get("results", []):
            print(
                f"\nProvider: {result.get('provider')}"
                f"\nEndpoint: {result.get('endpoint')}"
                f"\nDescription: {result.get('description')}"
                f"\nScore: {result.get('score')}"
                f"\nPrice: {result.get('price')}"
            )

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())