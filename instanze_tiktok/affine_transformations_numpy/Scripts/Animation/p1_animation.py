from instanim.scene import *




txt = text2D(
    'A', tag='ahmed',
    mainFont='ASAL1', 
    insertion=np.array([0, 0]),
    inputFontSize=100,
)
txt.set_fillColors(dsp.base.colors['crimson'])
txt.set_strokeColors(dsp.base.colors['plum'])
txt.set_strokeWidths(3)

txt.set_dotFills(False)
txt.set_dotStrokes(False)        

v_ = txt.shapes[0].exterior


area_ = area2D(exterior=v_, tag='area')


spc = space2D(area_, tag="space")
wndw = window2D(space=spc, zoom=1000, window = [np.array([[0, 0], [500, 0], [500, 500], [0, 500]])], tag='window')




# shp_.set_strokeWidth(3)
# shp_.set_dotStrokeWidth(1)
# shp_.display_no_segments() 
# shp_.area.hide()



class Translate(Action):

    def __init__(self,
        ent_tag, ent_par,
        dx=0, dy=0,
        start=0, dur=1,
        rateform_=rateform()
    ):
        swp_ = Sweep(
            ent_tag, ent_par,
            lambda t: ut.trans_3x3(dx*t, dy*t), # domain of paths are 0-1 (within span)
            start=start, dur=dur,
            delta='affine'
        )

        super().__init__(
            swp_,
            start=start, dur=dur, rateform_=rateform_
        )


class Scale(Action):

    def __init__(self,
        ent_tag, ent_par,
        sx=1, sy=1,
        start=0, dur=1,
        rateform_=rateform()
    ):

        swp_ = Sweep(
            ent_tag, ent_par,
            lambda t: ut.scale_3x3(ut.scale_per(sx, 1, t), ut.scale_per(sy, 1, t)), # domain of paths are 0-1 (within span)
            start=start, dur=dur,
            delta='affine'
        )

        super().__init__(
            swp_,
            start=start, dur=dur, rateform_=rateform_
        )


class Rotation(Action):

    def __init__(self,
        ent_tag, ent_par,
        ang=0,
        start=0, dur=1,
        rateform_=rateform()
    ):

        swp_ = Sweep(
            ent_tag, ent_par,
            lambda t: ut.rot_3x3(ang*t), # domain of paths are 0-1 (within span)
            start=start, dur=dur,
            delta='affine'
        )

        super().__init__(
            swp_,
            start=start, dur=dur, rateform_=rateform_
        )


class Shear(Action):

    def __init__(self,
        ent_tag, ent_par,
        kx=0, ky=0,
        start=0, dur=1,
        rateform_=rateform()
    ):

        swp_ = Sweep(
            ent_tag, ent_par,
            lambda t: ut.shear_3x3(kx*t, ky*t), # domain of paths are 0-1 (within span)
            start=start, dur=dur,
            delta='affine'
        )

        super().__init__(
            swp_,
            start=start, dur=dur, rateform_=rateform_
        )






shift_ = Translate(
    "area", "exterior", dx=100, dy=100,
    start=0, dur=3
)

scale_ = Scale(
    "area", "exterior", sx=10, sy=10,
    start=0, dur=3
)

rot_ = Rotation(
    "area", "exterior", ang=np.pi/2,
    start=0, dur=3
)


shear_ = Shear(
    "area", "exterior", kx=.5, ky=0,
    start=0, dur=3
)




# anim = Animation._2D(
#     [[area_, 'area']],
#     shift_, start=0, dur=3, tag='anim'
# )


# anim = Animation._2D(
#     [[area_, 'area']],
#     scale_, start=0, dur=3, tag='anim'
# )

# anim = Animation._2D(
#     [[area_, 'area']],
#     rot_, start=0, dur=3, tag='anim'
# )


anim = Animation._2D(
    [[wndw, 'window']],
    shift_, start=0, dur=3, tag='anim'
)

scn = Scene2D(anim, w=1000, h=1000, dur=3, tag='scene')
scn.preview(r'C:\Users\18055\Documents\Local_Repos\instanze\instanze_tiktok\affine_transformations_numpy\Scripts\Animation\outputs\translate', override=True)
# scn.preview(r'C:\Users\18055\Documents\Local_Repos\instanze\instanze_tiktok\affine_transformations_numpy\Scripts\Animation\outputs\scale', override=True)
# scn.preview(r'C:\Users\18055\Documents\Local_Repos\instanze\instanze_tiktok\affine_transformations_numpy\Scripts\Animation\outputs\rotate', override=True)
# scn.preview(r'C:\Users\18055\Documents\Local_Repos\instanze\instanze_tiktok\affine_transformations_numpy\Scripts\Animation\outputs\shear', override=True)


del area_, shift_, anim, scn



















# focusing on single sweep for single ent-par; scale for multiple ent-pars later...
class Affine(Action): 

    def __init__(self,
        ent_tag, ent_par, 
        *affine_seq,
        start=0, dur=1,
        rateform_=rateform()
    ):
        mat_seq = [] # sequence of operation matrices        
        for op in affine_seq:
            if not isinstance(op, list): raise ActionException('Each "operation" in a "affine_seq" must be packaged in a list.')

            len_op = len(op)
            if len_op<1: raise LenError('Packaged list must have one or more values.')

            op_type = op[0]

            if op_type=="+": # translation
                if len_op==1: mat = ut.trans_3x3(0, 0)
                elif len_op==2: 
                    # chk for op[1]?
                    mat = ut.trans_3x3(op[1], 0) 
                elif len_op==3:
                    # chk for op[1], op[2?
                    mat = ut.trans_3x3(op[1], op[2])                  
                else:
                    raise ActionException('Packaged list for translation "operation" ("+") must be one to three values where \n\
                        first is type, second is x-shift, and third is y-shift.')
            elif op_type=="*": # scale
                if len_op==1: mat = ut.scale_3x3(1, 1)
                elif len_op==2: 
                    # chk for op[1]?
                    mat = ut.scale_3x3(op[1], 1) 
                elif len_op==3:
                    # chk for op[1], op[2?
                    mat = ut.scale_3x3(op[1], op[2])                  
                else:
                    raise ActionException('Packaged list for scale "operation" ("*") must be one to three values where \n\
                        first is type, second is x-scale, and third is y-scale.')
            elif op_type=="r": # rotate
                if len_op==1: mat = ut.rot_3x3(0)
                elif len_op==2: 
                    # chk for op[1]?
                    mat = ut.rot_3x3(op[1])                
                else:
                    raise ActionException('Packaged list for rotate "operation" ("r") must be one to two values where \n\
                        first is type, and second is rotation-angle (radians).')
            elif op_type=="/": # shear
                if len_op==1: mat = ut.shear_3x3(1, 1)
                elif len_op==2: 
                    # chk for op[1]?
                    mat = ut.shear_3x3(op[1], 1) 
                elif len_op==3:
                    # chk for op[1], op[2?
                    mat = ut.shear_3x3(op[1], op[2])                  
                else:
                    raise ActionException('Packaged list for shear "operation" ("/") must be one to three values where \n\
                        first is type, second is x-shear, and third is y-shear.')                

            else: raise ActionException('Not a valid "operation" type specified.')

            mat_seq.append(mat)

            # product of all mat
            matP = mat_seq[0]
            for mat in mat_seq[1:]: matP = np.matmul(mat, matP)

            scale = Sweep(
                ent_tag, ent_par, 
                lambda t: ut.scale_3x3(3*t, 3*t),
                start=0, dur=3,
                delta='affine'
            )















