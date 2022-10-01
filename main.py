# from youtube_data import youtubestats
from yt_stats import YTstats
import argparse

category_dict = {
    # "Educational": {
        # "The_King_of_Random" : 'UC1zZE_kJ8rQHgLTVfobLi_g',
        # "National_Geographic": 'UCpVm7bg6pXKo1Pr6k5kxG9A',
        # "Crash_Course": 'UCaHx0T1LWrVKWF1XfWWLSuw',
        # "Ted-Ed": 'UCsooa4yRKGN_zEE8iknghZA',
        # "Matthew_Santoro": 'UCXhSCMRRPyxSoyLSPFxK7VA',
        # "Alltime10s": 'UCGi_crMdUZnrcsvkCa8pt-g',
        # "SciShow": 'UCZYTClx2T1of7BRZ86-8fow',
        # "Veritasium": 'UCHnyfMqiRRG1u-2MsSQLbXA',
        # "Mind_Warehouse": 'UCYenDLnIHsoqQ6smwKXQ7Hg',
        # "Khan_Academy": 'UC4a-Gbdw7vOaccHmFo40b9g',
        # 'vsauce' : 'UC6nSFpj9HTCZ5t-N3Rm3-HA',
        # 'c.g.p.grey' : 'UC2C_jShtL725hvbm1arSV9w',
        # 'national geographic' : 'UCpVm7bg6pXKo1Pr6k5kxG9A',
        # 'mit opencourse ware': 'UCEBb1b_L6zDS3xTUrIALZOw'
    # }
    # ,
    "Cooking": {
        # "Tasty": 'UCJFp8uSYCjXOMnkUyb3CQ3Q',
        # "Epic_Meal_Time": 'UCYjk_zY-iYR8YNfJmuzd70A',
        # "Jamie_Oliver": 'UCpSgg_ECBj25s9moCDfSTsA',
        # "How_ToCook_That": 'UCsP7Bpw36J666Fct5M8u-ZA',
        # "Binging_with_Babish": 'UCJHA_jMfCvEnv-3kRjTCQXw',
        # "Laura_in_the_Kitchen": 'UCNbngWUqL2eqRw12yAwcICg',
        # "MaangChi": 'UC8gFadPgK2r1ndqLI04Xvvw',
        # "JunsKitchen": 'UCRxAgfYexGLlu1WHGIMUDqw',
        # "Bon_Appetit": 'UCbpMy0Fg74eXXkvxJrtEn3w',
        # "SORTEDfood": 'UCfyehHM_eo4g5JUyWmms2LA'
        # 'new york times cooking': 'UC1rIOwTqDuWkFj87HZYRFOg',
        # 'pro home cook': 'UCzH5n3Ih5kgQoiDAQt2FwLw',
        # 'chef steps': 'UCxD2E-bVoUbaVFL0Q3PvJTg',
        # 'you suck at cooking': 'UCekQr9znsk2vWxBo3YiLq2w',
        # 'peaceful cuisine': 'UCQBG3PzyQKY8ieMG2gDAyOQ',
        # 'joshua weissman': 'UChBEbMKI1eCcejTtmI32UEw',
        # 'sam the cooking guy': 'UCbRj3Tcy1Zoz3rcf83nW5kw',
        'french cooking academy': 'UC0lG3Ihe4LGV851lODRIS5g',
        'everyday food': 'UCl0kP-Cfe-GGic7Ilnk-u_Q'
    }
    ,
    "Fitness_workout": {
        # "FitnessBlender": 'UCiP6wD_tYlYLYh3agzbByWQ',
        "blogilates": 'UCIJwWYOfsCfz6PjxbONYXSg',
        # "XHIT_Daily": 'UCM1Nde-9eorUhq-teaWlgUA',
        # "POPSUGAR_Fitness": 'UCBINFWq52ShSgUFEoynfSwg',
        # "ScottHermanFitness": 'UCEtMRF1ywKMc4sf3EXYyDzw',
        # "The_Fitness_Marshall": 'UCyqR7WkL8i1b6xtSssDmW9w',
        # "Guru_Mann_Fitness": 'UCGMOauU8dOd4mv2bT3Tx57w',
        # "Whitney_Simmons": 'UCEQi1ZNJiw3YMRwni0OLsTQ',
        # "Jordan_Yeoh_Fitness": 'UC4GJndVHEhdmqLFBHOCi97A',
        "Sascha_Fitness": 'UCiH4auDlkM0tgn9ewT3B1Vw',
        'Krissy Cela': 'UCl1Tkl0amPsxWJ1HLQdj92A',
        'Jeff Nippard' : 'UC68TLK0mAEzUyHx5x5k-S1Q',
        'chris heria' : 'UCaBqRxHEMomgFU-AkSfodCw',
        'MrandMrsMuscle' : 'UCJ2B_gnNWRE6QwgySgk-PlQ'
    }
    ,
    "Yoga": {
        # "Yoga_With_Adrienne": 'UCFKE7WVJfvaHW5q283SxchA',
        # "PsycheTruth": 'UCGb34D3ThpmjLNn-FLv2_yQ',
        # "Boho_Beautiful": 'UCWN2FPlvg9r-LnUyepH9IaQ',
        # "KinoYoga": 'UCH-81uaxCwAAaSgxRtxMkxg',
        # "Fightmaster_Yoga": 'UCcox27Gc-NGbb2-X9hdLaMw',
        # "SarahBethYoga": 'UC-0CzRZeML8zw4pFTVDq65Q',
        # "TaraStiles": 'UCa5OCJkZgtbIkaB1sA86XVA',
        # "Ekhart_Yoga": 'UCFYsO0t3zj0eJ_NcOlowTSA',
        # "DOYOUYOGA.com": 'UCEdFmnwp53XmtODotf788-Q',
        # "Yoga_By_Candace": 'UCI9s9nFu2m3K2CvhO2QVfTg',
        'blogilates': 'UCIJwWYOfsCfz6PjxbONYXSg',
        'Breathe and Flow' : 'UCbfPq-uRqonJQli41muSLeQ',
        'Move with Nicole' : 'UCEbbyBuyQiHpKiOMj9GFhVw',
        'eFit30' : 'UCFYbLvz0iXSzQjxr5UD9CxQ',
        'The Live Fit Girl': 'UCWkpYNGPaECjwXSy43c1egg'

    }
    ,
    # "History": {
        # "History_Channel": 'UC9MAhZQQd9egwWCxrwSIsJQ', #cannot fetch
        # "Alternate_History_Hub": 'UClfEht64_NrzHf8Y0slKEjw',
        # "Simple_History": 'UC510QYlOlKNyhy_zdQxnGYw',
        # "Oversimplified": 'UCNIuvl7V8zACPpTmmNIqP2A', #cannot fetch
        # "History_Buffs": 'UCggHoXaj8BQHIiPmOxezeWA',
        # "Timeline-World_History_Documentaries": 'UC88lvyJe7aHZmcvzvubDFRg',
        # "Overly_Sarcastic_Productions": 'UCodbH5mUeF-m_BsNueRDjcw',
        # "Historia_Civillis": 'UCv_vLHiWVBh_FR9vbeuiY-A',
        # "BazBattles": 'UCx-dJoP9hFCBloY9qodykvw',
        # "Feature_History": 'UCHdluULl5c7bilx1x1TGzJQ',
        # 'Weird History' : 'UCc-N24Y5OA0gqbjBwe1ttfA',
        # 'Tasting History with Max Miller': 'UCsaGKqPZnGp_7N80hcHySGQ',
        # 'The Great War': 'UCUcyEsEjhPEDf69RRVhRh4A',
        # 'The History Guy': 'UC4sEmXUuWIFlxRIFBRV6VXQ',
        # 'TIKhistory' : 'UCfZz8F37oSJ2rtcEJHM2kCg'

    # }
    # ,
    # "Science": {
        # "AsapSCIENCE": 'UCC552Sd-3nyi_tk2BudLUzA',
        # "Kurzgesagt": 'UCsXVk37bltHxD1rDPwtNM8Q',
        # "SmarterEveryDay": 'UC6107grRI4m0o2-emgoDnAA',
        # "minutephysics": 'UCUHW94eEFW7hkUMVaZz4eDg',
        # "TheBackYardScientist": 'UC06E4Y_-ybJgBUMtXx8uNNw',
        # "charlieissocoollike": 'UCmQXOAse-VnzuXHebX5I77g',
        # "Beyond Science": 'UCxo8ooAqXiObjuaIy10ud0A',
        # "Science Channel": 'UCvJiYiBUbw4tmpRSZT2r1Hw',
        # "IncredibleScience": 'UCJcycnanWtyOGcz34jUlYZA',
        # "Science Insider": 'UC9uD-W5zQHQuAVT2GdcLCvg',
        # '3Blue1Brown' : 'UCYO_jab_esuFRV4b17AJtAw',
        # 'Physics Videos by Eugene Khutoryansky': 'UCJ0yBou72Lz9fqeMXh9mkog',
        # 'acapellascience' : 'UCTev4RNBiu6lqtx8z1e87fQ',
        # 'Lectures by Walter Lewin' : 'UCiEHVhv0SBMpP75JbzJShqw',
        # 'The Science Asylum': 'UCXgNowiGxwwnLeQ7DXTwXPg'
    # }
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
        # 'Al Jazeera English': 'UCNye-wNBqNL5ZzHSJj3l8Bg',
        # 'Fox News': 'UCXIJgqnII2ZOINSWNOGFThA',
        # "CBS News" : 'UC8p1vwvWtl6T73JiExfWs1g',
        # 'US Military News' : 'UC0bpxzOXueQV7rRPomDiX8A'
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
        # 'Trap Nation' : 'UCa10nxShhzNrCE1o2ZOPztg',
        # 'No Copyright Sounds': 'UC_aEa8K-EOJ3D6gOs7HcyNg',
        # 'Ultra Music': 'UC4rasfm9J-X4jNl9SvXp8xA',
        # 'Audio Library': 'UCht8qITGkBvXKsR1Byln-wA',

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
        # "Rclbeauty101": 'UCB0d0JLn1WcGYcwwZ87d2LA', ##unable to fetch
        # "CollegeHumor": 'UCPDXXXJj9nax0fr0Wfc048g',
        # "Lele Pons": 'UCi9cDo6239RAzPpBZO9y5SA',
        # 'Nigahiga': 'UCSAUGyc_xA8uYzaIVG6MESQ',
        # 'BFvsGF': 'UCgefQJC5UgbWJHDxBqB4qVg',
        # 'Bart Baker': 'UCazMm3tOCkYrIGE_17j0mVg',
        # 'Thelonelyisland': 'UCCHcEUksSVKsRDH86j77Ntg',
        # 'ExplosmEntertainment':'UCWXCrItCF6ZgXrdozUS-Idw'
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
        # 'Mark Abroad':'UCxkF42nqXoZ0sZP-GqU-Cww',
        # 'Drew Binsky': 'UC0Ize0RLIbGdH5x4wI45G-A',
        # 'ARIENNE PARZEI': 'UCH2X0QCXlWNfBC7RpPNfe0g',
        # 'Going Awesome Places': 'UCKCRueDLpzx1vBcQHCc4ZHA',
        # 'Be My Travel Muse': 'UCVdvbdhaXo01c1G4mNp1RsQ'
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
