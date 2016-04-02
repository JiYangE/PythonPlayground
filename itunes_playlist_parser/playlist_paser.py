from plistlib import readPlist
from os import path
from matplotlib import pyplot
import numpy as np


class PlayListParser:

    def __init__(self, filename):
        self.filename = filename
        self.plist = readPlist(self.filename)

    def find_dupilicates(self, plist):
        print('Finding duplicate tracks in %s...' % self.filename)
        tracks = plist['Tracks']
        track_names = {}
        for id, track in tracks.items():
            try:
                name = track['Name']
                duration = track['Total Time']
                # print name, duration
                if name in track_names:
                    exist_duration = track_names[name][0]
                    if duration // 1000 == exist_duration // 1000:
                        count = track_names[name][1]
                        track_names[name] = (duration, count + 1)
                else:
                    track_names[name] = (duration, 1)
            except:
                print('Something wrong, check it again.')
        return track_names

    def extract_duplicates(self, track_dict):
        dups = []
        for key, value in track_dict.items():
            if value[1] > 1:
                dups.append((value[1], key))
        if len(dups) > 0:
            f = open('dups.txt', 'w')
            print('Found %d results. Saved to %s' % (len(dups), 'dups.txt'))
            for val in dups:
                f.write(str(val[0]) + ' ' + str(val[1]) + '\n')
            f.close()
        else:
            print('There is no duplicate track!')
        return dups

    def find_common_track(self, filenames):
        track_name_set = []
        for filename in filenames:
            track_set = set()
            plist = readPlist(filename)
            tracks = plist['Tracks']
            for id, track in tracks.items():
                try:
                    track_set.add(track['Name'])
                except:
                    pass
            track_name_set.append(track_set)
        common_tracks = set.intersection(*track_name_set)
        if len(common_tracks) > 0:
            f = open('common.txt', 'w')
            print('Found %d results. Data saved to %s'
                  % (len(common_tracks), 'common.txt'))
            for val in common_tracks:
                f.write((val + '\n').encode('UTF-8'))
            f.close()
        else:
            print('There is no duplicate track!')

    def plot_stats(self, plist):
        tracks = plist['Tracks']
        ratings = []
        durations = []
        for id, track in tracks.items():
            try:
                ratings.append(track['Album Rating'])
                durations.append(track['Total Time'])
            except:
                pass
        if ratings is [] or durations is []:
            print('No valid data input')
            return
        x = np.array(durations, np.int32)
        x = x / 60000.0
        y = np.array(ratings, np.int32)
        # plot 1
        pyplot.subplot(2, 1, 1)
        pyplot.plot(x, y, 'o')
        pyplot.axis([0, 1.05 * np.max(x), -1, 110])
        pyplot.xlabel('Duration')
        pyplot.ylabel('Rating')
        # plot 2
        pyplot.subplot(2, 1, 2)
        pyplot.hist(x, bins=20)
        pyplot.xlabel('Duration')
        pyplot.ylabel('Count')

        pyplot.show()

    def run(self):
        track_dict = self.find_dupilicates(self.plist)
        # print(track_dict)
        dups = self.extract_duplicates(track_dict)
        try:
            self.plot_stats(self.plist)
        except:
            pass
        common_filename = []
        print('You can find common tracks in diff files.')
        print('Enter the filename one by one.')
        while True:
            fname = raw_input('Filename -> ')
            if fname == 'q':
                break
            else:
                common_filename.append(fname)
        if len(common_filename) > 1:
            self.find_common_track(common_filename)

if __name__ == "__main__":
    while True:
        filename = raw_input('Enter the filename: ')
        if '.' not in filename:
            filename += '.xml'
        if path.isfile(filename):
            break
        else:
            print(filename, "does not exist")
    parser = PlayListParser(filename)
    parser.run()
