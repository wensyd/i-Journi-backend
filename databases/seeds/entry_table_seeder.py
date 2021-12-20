"""EntryTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Entry import Entry

class EntryTableSeeder(Seeder):
    def run(self):
      Entry.create({"date": "12/23/2021", "title": "This is the first entry", "body":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ornare nunc lacinia, mollis dolor eget, aliquet libero. In nunc nibh, lobortis sed felis sed, lobortis pretium tellus. Nam enim leo, fringilla vel lorem in, dictum sodales ligula. Quisque sed lacinia orci, vitae efficitur orci. Integer tincidunt vulputate mi non interdum. Cras laoreet consectetur purus, in luctus dolor faucibus et. Nullam at mi volutpat dolor hendrerit malesuada. Vestibulum suscipit mauris ut tempor venenatis. Sed a dui sed diam tempus bibendum. Quisque elementum nisi porta viverra lobortis. Vivamus tempus ex ut leo dignissim varius."})
      Entry.create({"date": "12/23/2021", "title": "This is the second entry", "body":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ornare nunc lacinia, mollis dolor eget, aliquet libero. In nunc nibh, lobortis sed felis sed, lobortis pretium tellus. Nam enim leo, fringilla vel lorem in, dictum sodales ligula. Quisque sed lacinia orci, vitae efficitur orci. Integer tincidunt vulputate mi non interdum. Cras laoreet consectetur purus, in luctus dolor faucibus et. Nullam at mi volutpat dolor hendrerit malesuada. Vestibulum suscipit mauris ut tempor venenatis. Sed a dui sed diam tempus bibendum. Quisque elementum nisi porta viverra lobortis. Vivamus tempus ex ut leo dignissim varius."})
      Entry.create({"date": "12/23/2021", "title": "This is the third entry", "body":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ornare nunc lacinia, mollis dolor eget, aliquet libero. In nunc nibh, lobortis sed felis sed, lobortis pretium tellus. Nam enim leo, fringilla vel lorem in, dictum sodales ligula. Quisque sed lacinia orci, vitae efficitur orci. Integer tincidunt vulputate mi non interdum. Cras laoreet consectetur purus, in luctus dolor faucibus et. Nullam at mi volutpat dolor hendrerit malesuada. Vestibulum suscipit mauris ut tempor venenatis. Sed a dui sed diam tempus bibendum. Quisque elementum nisi porta viverra lobortis. Vivamus tempus ex ut leo dignissim varius."})