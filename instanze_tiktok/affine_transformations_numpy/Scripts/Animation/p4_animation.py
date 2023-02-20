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
wndw = window2D(space=spc, zoom=1000, tag='window')


class Affine(Action):

    def __init__(self,
        ent_tag, ent_par,
        *affine_seq,
        start=0, dur=1,
        rateform_=rateform()
    ):
        mat_seq=[] # sequence of operation matrices
        for op in affine_seq:
            if not isinstance(op, list):
                raise ActionException('Each operation in a "affine_seq" must be packaged in a list.')

            len_op = len(op)
            if len_op<1: raise LenError('Packaged list must have one or more values.')

            op_type = op[0]

            if op_type=="+": # translation
                if len_op==2:
                    mat = ut.trans_3x3(op[1], 0)
                elif len_op==1:
                    mat = ut.trans_3x3(0, 0)
                elif len_op==3:
                    mat = ut.trans_3x3(op[1], op[2])
                else:
                    raise ActionException('Packaged list for translation "operation" ("+") must be one to three values where \n\
                        first is type, second is x-shift, and third is y-shift.')
            elif op_type=="*": # scale
                if len_op==1: mat = ut.scale_3x3(1, 1)
                elif len_op==2:
                    mat = ut.scale_3x3(op[1], 1)
                elif len_op==3: mat = ut.scale_3x3(op[1], op[2])
                else:
                    raise ActionException('Packaged list for scale "operation ("*") must be one to three values where \n\
                        first is type, second is x-scale, and third is y-scale')
            elif op_type=="r": # rotate
                if len_op==1: mat = ut.rot_3x3(0)
                elif len_op==2:
                    mat = ut.rot_3x3(op[1])
                else: raise ActionException('Packaged list for rotate "operation" ("r") must be one to two values where \n\
                    first is type, and second is rotation-angle (radians).')
            