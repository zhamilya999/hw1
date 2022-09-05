import asyncio
from time import sleep

# async def download_photo(photo_count):
#     while True:
#         photo_count += 1
#         await  asyncio.sleep(1)
#         print(f"Photo number {photo_count}...")
#
#
# async def download_video(video_count):
#     while True:
#         video_count += 1
#         await asyncio.sleep(5)
#         print(f"Video number {video_count}...")
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_photo(photo_count),
#         download_video(video_count)
#     ]
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())

def download_photo(current_photo):
    sleep(1)
    print(f"Download photo {current_photo}....")


def main():
    count = int(input("Enter amount:"))
    current_photo = 0

    while current_photo < count:
        current_photo+=1
        download_photo(current_photo)

    print("Done!")

