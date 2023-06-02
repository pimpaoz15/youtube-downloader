from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

#Getting the highest resolution
# ys = yt.streams.get_highest_resolution()
ys = yt.streams.filter(res="720p")

#Starting download
print("Downloading...")

# ADD FOLDER HERE
ys.download('/Users/pimpao/Library/CloudStorage/OneDrive-Personal/VSCode/Python')

print("Download completed!!")
