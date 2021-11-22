from django_cron import CronJobBase, Schedule
from django.conf import settings
from datetime import datetime,timedelta
from googleapiclient.discovery import build
import apiclient

from AppApi.models import VideoInfo


class CallYoutubeAPI(CronJobBase):
    RUN_EVERY_MINS = 0.5 #Duration set to 30 sec

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'AppApi.Call_Youtube_API'    # a unique code

    def do(self):
        apiKey = settings.YOUTUBE_DATA_API_KEY
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=0.5)

        youtube =build("youtube", "v3", developerKey=apiKey)
        req = youtube.search().list(q="cricket", part="snippet", order="date", maxResults=50,
                                    publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z')) #Parameters like q,part ,#order,maxResults are predefined # in youtube developer section
        res = req.execute()                                                                                    
        
        #Extracting the information that we require as per the parameters of the model we have defined in models section
        
        for item in res['items']:
            video_id = item['id']['videoId']
            publishedDateTime = item['snippet']['publishedAt']
            title = item['snippet']['title']
            description = item['snippet']['description']
            thumbnailsUrls = item['snippet']['thumbnails']['default']['url']

            # Creating Object in Databse

            VideoInfo.objects.create(
                video_id=video_id,
                title=title,
                description=description,
                publishedDateTime=publishedDateTime,
                thumbnailsUrls=thumbnailsUrls,
            )
        