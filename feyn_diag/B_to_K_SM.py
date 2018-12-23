# EW  penguin 
#	       	/__
#	       /
#            _/
# in1 ------(_)------ out1a
#             
#             
#                    
# in2 ---------------out2b
#
import pyx
from pyfeyn.user import *
processOptions()
fd = FeynDiagram()
in1 = Point(1, 7)
loop_in = Vertex(4, 7)
loop_out = Vertex(7, 7)
out1a = Point(11, 7)
out1b = Point(11, 9)
in2 = Point(1, 0)
out2a = Point(11, 9)
out2 = Point(11, 0)
out1c = Vertex(out1b.x() + 2, out1b.y())
out1d = Vertex(out2a.x() - 2, out2a.y())
outl = Point(11,9 )
outal = Point(11, 13)
vtx = Vertex(9,11)

f_spec = Fermion(out2, in2).addArrow().addLabel(r"\APdown",size= pyx.text.size.Huge)
f1 = Fermion(in1, loop_in).addArrow().addLabel(r"\Pbottom",size= pyx.text.size.Huge)
f2 = Fermion(loop_out, out1a).addArrow().addLabel(r"\Pstrange",size= pyx.text.size.Huge)
bos1 = Photon(loop_in, loop_out).bend(+1.5).addLabel(r"\PWminus",size= pyx.text.size.Huge)
f_loop = Fermion(loop_in, loop_out).bend(-1.5).addArrow() \
         .addLabel(r"\Pup,\,\Pcharm,\,\Ptop",displace =+0.5,size= pyx.text.size.Huge)
bos2 = Photon(f_loop.fracpoint(0.5), vtx).addLabel(r"\Pphoton/\PZ", displace=0.5,size= pyx.text.size.Huge) #.bend(0.5)
f3 = Fermion(vtx, outl).addArrow().addLabel(r"\Plepton",size= pyx.text.size.Huge)
f4 = Fermion(outal,vtx).addArrow().addLabel(r"\APlepton",size= pyx.text.size.Huge)

in_blob = Ellipse(x=1, y=3.5, xradius=1, yradius=3.5).setFillStyle(CROSSHATCHED45)
out_blob1 = Ellipse(x=11, y=3.5, xradius=1, yradius=3.5).setFillStyle(HATCHED135)


fd.draw("B_to_K_SM.pdf")


