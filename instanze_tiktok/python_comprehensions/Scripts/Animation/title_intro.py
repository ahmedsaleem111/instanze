import unittest
import time

from instanim.scene import *




        
if __name__ == "__main__":


    txt = text2D(
        'Comprehensions', tag='ahmed',
        mainFont='Consolas', 
        insertion=np.array([200, 500]),
        inputFontSize=90,
    )

    txt_io_start = time.time()

    txt.hide_areas()
    txt.hide_dots()
    txt.display_no_segments()

    acts_ = []
    for shp_ in txt.shapes:
        assert isinstance(shp_, shape2D)

        sub_acts = []

        shp_tag = shp_.tag
        v_ = shp_.exterior
        for i, hole in enumerate(shp_.holes):
            sub_acts.append(
                Sweep(
                    shp_tag+'_hole_'+str(i), 'pathSubsets', 
                    np.array([[0, len(hole)]]),
                    delta='displace_linear'
                )
            )
            sub_acts.append(
                Sweep(
                    shp_tag+'_hole_'+str(i), 'dotsSubsets', 
                    np.array([[0, len(hole)]]),
                    start=0, dur=3,
                    delta='displace_linear'
                )
            )

        sub_acts.append(
            Sweep(
                shp_tag+'_exterior', 'pathSubsets', 
                np.array([[0, len(v_)]]),
                delta='displace_linear'
            )
        )
        sub_acts.append(
            Sweep(
                shp_tag+'_exterior', 'dotsSubsets', 
                np.array([[0, len(v_)]]),
                delta='displace_linear'
            )
        )
        sub_acts.append(
            Sweep(
                shp_tag+'_area', 'areaFillAlpha', 
                dsp.alpha(1),
                delta='displace_linear'
            )
        )

        acts_.append(Action(*sub_acts, scales=scaleConstant(1)))

    textIn = Action(
        *acts_,
        start=0, dur=3, scales=scaleConstant(.5)
    )


    acts_ = []
    for shp_ in txt.shapes:
        assert isinstance(shp_, shape2D)

        sub_acts = []

        shp_tag = shp_.tag
        v_ = shp_.exterior
        for i, hole in enumerate(shp_.holes):
            sub_acts.append(
                Sweep(
                    shp_tag+'_hole_'+str(i), 'pathSubsets', 
                    np.array([[0, 0]]),
                    delta='displace_linear'
                )
            )
            sub_acts.append(
                Sweep(
                    shp_tag+'_hole_'+str(i), 'dotsSubsets', 
                    np.array([[0, 0]]),
                    start=0, dur=3,
                    delta='displace_linear'
                )
            )

        sub_acts.append(
            Sweep(
                shp_tag+'_exterior', 'pathSubsets', 
                np.array([[0, 0]]),
                delta='displace_linear'
            )
        )
        sub_acts.append(
            Sweep(
                shp_tag+'_exterior', 'dotsSubsets', 
                np.array([[0, 0]]),
                delta='displace_linear'
            )
        )
        sub_acts.append(
            Sweep(
                shp_tag+'_area', 'areaFillAlpha', 
                dsp.alpha(0),
                delta='displace_linear'
            )
        )

        acts_.append(Action(*sub_acts, scales=scaleConstant(1)))

    textOut = Action(
        *acts_,
        start=5, dur=3, scales=scaleConstant(.5)
    )



    anim = Animation._2D(
        [[txt, 'ahmed']],
        textIn, textOut, start=0, dur=9, tag='anim'
    )

    scn = Scene2D(anim, dur=9, tag='scene', background_alpha=dsp.alpha(0))
    scn.preview(r'C:\Users\18055\Documents\Local_Repos\instanze\instanze_tiktok\python_comprehensions\Scripts\Animation\outputs\title_intro', override=True)

    del textIn, anim, scn

    txt_io_end = time.time()

    print('\n')
    print('   >> Time elapsed for program run: '+str(txt_io_end-txt_io_start)+'s')
    print('\n\n')


