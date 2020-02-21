# coding=gbk
import unreal

"""
Usage:

import sequencer_test as se
se.NAME
se.Hello()

reload(sequencer_test)
"""
NAME = 'wangbo'


def Hello():
    """
    Only for test.
    :return:
    """
    print('-=WB=- hahaha')
    sequence_path = '/Game/Kaiju/Sequence_Kaiju'
    sequence_asset = unreal.LevelSequence.cast(unreal.load_asset(sequence_path))
    print('sequence = ', sequence_asset)
    tracks = sequence_asset.get_master_tracks()
    tracks_num = len(tracks)
    track_0_name = tracks[0].get_display_name()
    # track_0_option = tracks[0].dis
    print('tracks: num, name, type = ', tracks_num, str(track_0_name), type(tracks[0]))
    print('~~~~~~~~~~~~~~~~~~~~~+++')
    sequence_obj = unreal.MovieSceneSequence()  # 单件
    sequence_obj_name = sequence_obj.get_display_name()
    print(sequence_obj)
    print('sequence_obj_name : ', sequence_obj_name)
    print('~~~~~~~~~~~~~~~~~~~~~+++')
    # master_tracks = sequence_obj.get_master_tracks()
    # possessables = sequence_obj.get_possessables()
    # print(possessables)
