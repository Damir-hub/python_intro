# run_api.py
import time
from api_client import fetch_get, fetch_post, fetch_put, fetch_delete

def main():
    start = time.perf_counter()

    status, data = fetch_get()
    print(f"GET Status Code: {status}")
    print(f"GET Response: {data}")

    status, data = fetch_post()
    print(f"POST Status Code: {status}")
    print(f"POST Response: {data}")

    status, data = fetch_put()
    print(f"PUT Status Code: {status}")
    print(f"PUT Response: {data}")

    status, data = fetch_delete()
    print(f"DELETE Status Code: {status}")
    print(f"DELETE Response: {data}")

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds.")

if __name__ == "__main__":
    main()
