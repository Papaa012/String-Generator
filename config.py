from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "7782147"))
API_HASH = getenv("API_HASH", "807b64fbb57797086097d274df3a934c")

BOT_TOKEN = getenv("BOT_TOKEN", "5855940486:AAFTV29GPkDA1rV9WbU9l3ZaCwhtxZE0wmw")
OWNER_ID = int(getenv("OWNER_ID", "1820525265"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://alone:hacker@cluster0.hg3tgr7.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "TEAM_XTRON")

SESSION = getenv("SESSION", "BQCKHGhvtK5ufCVxmHBNKQmoonaX09MUoe_oHblkpuZCFxDuhSEv4_NF30tXTgobh8sCKOXlQb1g7v67pq92pe6Z2F8j4k8UxAu_MVjZDfT6mcTnoOhB2C4bSycEC1OJY-3QD_FNlMxouZvbeVMkVdRI0pR-oh0ooPZmfmZNzb1GVDNnveQQiR6Pgs-S95l_yQfGmQa5j6SGYLwyeIs8AkjRblwBIFOZ9sjuqGLaZ2lbk4bkudEDxJlvxeomdiGgFwP2hyYZ7OsDRmewn3G-S9KsEOJMkh4z6tJNJZX6i61wOutEHR0SXKYj9lD0MSw4O6YElOgxXBG8Hb7OIfTJZmNJAAAAAXM7rskA")
