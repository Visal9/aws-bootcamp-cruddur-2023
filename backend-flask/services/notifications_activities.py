import logging
from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class NotificationsActivities:
    def __init__(self, xray_recorder):
        self.xray_recorder=xray_recorder
    
    @xray_recorder.capture('notification-activities-data')
    def run(self):
        xray_recorder.current_segment().put_annotation('Service','Notifications')
        now = datetime.now(timezone.utc).astimezone()
        results = [{
            'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle':  'FruitPie',
            'message': 'Fun Fun Fun',
            'created_at': (now - timedelta(days=2)).isoformat(),
            'expires_at': (now + timedelta(days=5)).isoformat(),
            'likes_count': 5,
            'replies_count': 2,
            'reposts_count': 0,
            'replies': [{
                'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                'handle':  'Worf',
                'message': 'This post has no honor!',
                'likes_count': 0,
                'replies_count': 0,
                'reposts_count': 0,
                'created_at': (now - timedelta(days=2)).isoformat()
                }],
            }]
        xray_recorder.current_segment().put_metadata('Data', {'length': len(results), 'fetched-time': now})
        return results
