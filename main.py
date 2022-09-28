# from youtube_data import youtubestats
from yt_stats import YTstats
import argparse

category_dict = {
    "Educational": {
        # "The_King_of_Random" : 'UC1zZE_kJ8rQHgLTVfobLi_g',
        # "National_Geographic": 'UCpVm7bg6pXKo1Pr6k5kxG9A',
        # "Crash_Course": 'crashcourse',
        # "Ted-Ed": 'UCsooa4yRKGN_zEE8iknghZA',
        # "Matthew_Santoro": 'UCXhSCMRRPyxSoyLSPFxK7VA',
        # "Alltime10s": 'UCGi_crMdUZnrcsvkCa8pt-g',
        # "SciShow": 'UCZYTClx2T1of7BRZ86-8fow',
        # "Veritasium": 'UCHnyfMqiRRG1u-2MsSQLbXA',
        # "Mind_Warehouse": 'UCYenDLnIHsoqQ6smwKXQ7Hg',
        "Khan_Academy": 'UC4a-Gbdw7vOaccHmFo40b9g'
    }
    ,
    "Cooking": {
        "Tasty": 'UCJFp8uSYCjXOMnkUyb3CQ3Q',
        "Epic_Meal_Time": 'EpicMealTime',
        "Jamie_Oliver": 'JamieOliver',
        "How_ToCook_That": 'howtocookthat',
        "Binging_with_Babish": 'bgfilms',
        "Laura_in_the_Kitchen": 'LauraVitalesKitchen',
        "MaangChi": 'Maangchi',
        "JunsKitchen": 'JunsKitchen',
        "Bon_Appetit": 'BonAppetitDotCom',
        "SORTEDfood": 'sortedfood'
    }
    ,
    "Fitness_workout": {
        "FitnessBlender": 'FitnessBlender',
        "blogilates": 'blogilates',
        "XHIT_Daily": 'XFitDaily',
        "POPSUGAR_Fitness": 'popsugartvfit',
        "ScottHermanFitness": 'ScottHermanFitness',
        "The_Fitness_Marshall": 'TheFitnessMarshall',
        "Guru_Mann_Fitness": 'UCGMOauU8dOd4mv2bT3Tx57w',
        "Whitney_Simmons": 'UCEQi1ZNJiw3YMRwni0OLsTQ',
        "Jordan_Yeoh_Fitness": 'jordanyeohfitness',
        "Sascha_Fitness": 'saschafitness',
    }
    ,
    "Yoga": {
        "Yoga_With_Adrienne": 'yogawithadriene',
        "PsycheTruth": 'psychetruth',
        "Boho_Beautiful": 'cexercize',
        "KinoYoga": 'KinoYoga',
        "Fightmaster_Yoga": 'lesleyfightmaster',
        "SarahBethYoga": 'SarahBethShow',
        "TaraStiles": 'TaraStilesYoga',
        "Ekhart_Yoga": 'yogatic',
        "DOYOUYOGA.com": 'DoYouYoga',
        "Yoga_By_Candace": 'yogabycandace',
    }
    ,
    "History": {
        # "History_Channel": 'HISTORY', #cannot fetch
        # "Alternate_History_Hub": 'AlternateHistoryHub', #cannot fetch
        # "Simple_History": 'UC510QYlOlKNyhy_zdQxnGYw',
        # "Oversimplified": 'Webzwithaz', #cannot fetch
        # "History_Buffs": 'UCggHoXaj8BQHIiPmOxezeWA',
        # "Timeline-World_History_Documentaries": 'UC88lvyJe7aHZmcvzvubDFRg',
        # "Overly_Sarcastic_Productions": 'RedEyesTakeWarning', #cannot fetch
        # "Historia_Civillis": 'UCv_vLHiWVBh_FR9vbeuiY-A',
        # "BazBattles": 'UCx-dJoP9hFCBloY9qodykvw',
        "Feature_History": 'UCHdluULl5c7bilx1x1TGzJQ',
    }
    ,
    "Science": {
        "AsapSCIENCE": 'AsapSCIENCE',
        "Kurzgesagt": 'Kurzgesagt',
        "SmarterEveryDay": 'destinws2',
        "minutephysics": 'minutephysics',
        "TheBackYardScientist": 'TheBackyardScientist',
        "charlieissocoollike": 'charlieissocoollike',
        "Beyond Science": 'beyondsciencetv',
        "Science Channel": 'ScienceChannel',
        "IncredibleScience": 'IncredibleScience',
        "Science Insider": 'UC9uD-W5zQHQuAVT2GdcLCvg',
    }
    # ,
    # "News": {
        # "Vice": 'UCn8zNIfYAQNdrFRrr8oibKw',
        # "IndiaTV": 'UCttspZesZIDEwwpVIgoZtWQ',
        # "Barcroft_TV": 'UCfwx98Wty7LhdlkxL5PZyLA',
        # "CNN": 'UCupvZG-5ko_eiXAupbDfxWw',
        # "Vox": 'UCLXo7UDZvByw2ixzpQCufnA',
        # "ABS-CBN_News": 'UCE2606prvXQc_noEqKxVJXA',
        # "Inside_Edition": 'UC9k-yiEpRHMNVOnOi_aQK8w',
        # "ABC_News": 'UCBi2mrWuNuyYy4gbM6fU18Q',
        # "The_Young_Turks": 'UC1yBKRuGpC1tSM73A0ZjYjQ',
        # "BBC_News": 'UC16niRr50-MSBwiO3YDb3RA',
    # }
    # ,
    # "Music": {
        # "Ed Sheeran": 'UC0C-w0YjGpqDXGB8IHb662A',
        # "Eminem": 'UCfM3zsQsOnfWNUppiycmBuw',
        # "Katy Perry": 'UCYvmuw-JtVrTZQ-7Y4kd63Q',
        # "Taylor Swift": 'UCqECaJ8Gagnn7YCbPEzWH6g',
        # "One Direction": 'UCb2HGwORFBo94DmRx4oLzow',
        # "Ariana Grande": 'UC9CoOnJkIBMdeijd9qYoT_g',
        # "Spinnin’ Records": 'UCpDJl2EmP7Oh90Vylx0dZtA',
        # "Trap Nation": 'UCa10nxShhzNrCE1o2ZOPztg',
        # "Bruno Mars": 'UCoUM-UJ7rirJYP8CQ0EIaHA',
        # "Marshmello": 'UCEdvpU2pFRCVqU6yIPyTpMQ',
    # }
    # ,
    # "Comedy": {
        # "Smosh": 'UCY30JRSgfhYXA6i6xX1erWg',
        # "shane": 'UCV9_KinVpV-snHe3C3n1hvA',
        # "JennaMarbles": 'UC9gFih9rw0zNCK3ZtoKQQyA', ##300 videos left here
        # "The Tonight Show Starring Jimmy Fallon": 'UC8-Th83bH_thdKZDJCrn88g',
        # "Liza Koshy": 'UCxSz6JVYmzVhtkraHWZC7HQ',
        # "Super Woman": 'UCfm4y4rHF5HGrSr-qbvOwOg',
        # "FailArmy": 'UCPDis9pjXuqyI7RYLJ-TTSA',
        # "Rclbeauty101": 'Rclbeauty101', ##unable to fetch
        # "CollegeHumor": 'UCPDXXXJj9nax0fr0Wfc048g',
        # "Lele Pons": 'UCi9cDo6239RAzPpBZO9y5SA',
    # }
    # ,
    # "Travel": {
        # "INSIDER": 'UCHJuQZuzapBh-CuhRYxIZrg',
        # "Mark Wiens": 'UCyEd6QBSgat5kkC6svyjudA',
        # "George Benson": 'UCdPambxHRj0kdFPNoJFM98A',
        # "Collin Abroadcast": 'UCXsQlHGuoWqukC9vz-uonrg',
        # "High On Life": 'UCd5xLBi_QU6w7RGm5TTznyQ',
        # "Expedia": 'UCGaOvAFinZ7BCN_FDmw74fQ',
        # "Miss Mina": 'UC8hI77bH0VraIw6p2PHwivQ',
        # "Chonnyday": 'UC_ptyMRLOsS1Uj0a34a_xCA',
        # "Stories": 'UCJsSEDFFnMFvW9JWU6XUn0Q',
        # "Rick Steves Europe": 'UCchgIh8Tc4sTmBfnMQ5pDdg',
    # }
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("API_KEY", metavar="key", type=str, help="supply youtube API Key.")

    args = parser.parse_args()

    category = input(
        "Type in a category from the following (case-sensitive)\n{0}\n".format(str(list(category_dict.keys()))))
    API_KEY = args.API_KEY

    for _, channel_id in category_dict[category].items():
        yt = YTstats(API_KEY, channel_id)
        yt.extract_all()
        yt.dump(category)
    # dumps to .json
