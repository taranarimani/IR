class News:
    gid = 0

    def __init__(self, date, title, url, summary, meta_tags, content):
        self.date = date
        self.title = title
        self.url = url
        self.summary = summary
        self.meta_tags = meta_tags
        self.content = content

        self.id = self.gid
        self.gid += 1

    def __str__(self):
        return "\n" + self.date + ",\n" + self.title + ",\n" + self.url + ",\n" + \
            self.summary + ",\n" + self.meta_tags + ",\n" + self.content + "\n"
