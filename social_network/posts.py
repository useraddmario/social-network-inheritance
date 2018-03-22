from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        # I used the datetime.utcnow() from the answer, but I originally used datetime.datetime.now()
        self.timestamp = timestamp or datetime.utcnow()
        self.user = None

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
         

    def __str__(self):
        # I had a similar solution, but had no idea how to remove the "" from self.text, I was trying self.text.strip('"')
        return '@{first_name} {last_name}: "{text}"\n\t{date}'.format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            date=self.timestamp.strftime("%A, %b %d, %Y"))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url
        
    def __str__(self):
        # I had a similar solution, but had no idea how to remove the "" from self.text, I was trying self.text.strip('"')
        return '@{first_name} {last_name}: "{text}"\n\t{img}\n\t{date}'.format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            img=self.image_url,
            date=self.timestamp.strftime("%A, %b %d, %Y"))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        # I had a similar solution, but had no idea how to remove the "" from self.text, I was trying self.text.strip('"')
        return ('@{first_name} Checked In: "{text}"'
                '\n\t{coordinates}\n\t{date}').format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            text=self.text,
            coordinates="{}, {}".format(self.latitude, self.longitude),
            date=self.timestamp.strftime("%A, %b %d, %Y"))
