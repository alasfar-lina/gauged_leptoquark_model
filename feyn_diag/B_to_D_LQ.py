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

fd = FeynDiagram()
in1 = Point(1, 7)
loop_in = Vertex(6.5, 7)
loop_out = Vertex(7, 7)
out1a = Point(7, 11)
out1b = Point(11, 9)
in2 = Point(1, 0)
out2a = Point(11, 9)
out2 = Point(13, 0)
out1c = Vertex(out1b.x() + 2, out1b.y())
out1d = Vertex(out2a.x() - 2, out2a.y())
outl = Point(13,7 )
outal = Point(10, 11)
vtx = Vertex(9.5,7)

f_spec = Fermion(out2, in2).addArrow().addLabel(r"\APquark",size= pyx.text.size.Huge )
f1 = Fermion(in1, loop_in).addArrow().addLabel(r"\Pbottom",size= pyx.text.size.Huge )
f2 = Fermion(loop_in, out1a).addArrow().addLabel(r"\Ptauon",size= pyx.text.size.Huge )
# bos1 = Photon(loop_in, loop_out).bend(+1.5).addLabel(r"\PWplus")
# f_loop = Fermion(loop_in, loop_out).bend(-1.5).addArrow() \
#          .addLabel(r"\Pup,\,\Pcharm,\,\Ptop",displace =+0.5)
bos = Photon(loop_in, vtx).addLabel(r"$V^{+}$", displace=0.5,size= pyx.text.size.Huge ) #.bend(0.5)
f3 = Fermion(vtx, outl).addArrow().addLabel(r"\Pcharm",size= pyx.text.size.Huge )
f4 = Fermion(outal,vtx).addArrow().addLabel(r"\APnu",displace=0.3,size= pyx.text.size.Huge )

in_blob = Ellipse(x=1, y=3.5, xradius=1, yradius=3.5).setFillStyle(CROSSHATCHED45)
out_blob2 = Ellipse(x=13, y=3.5, xradius=1, yradius=3.5).setFillStyle(HATCHED135)
#Label("D")


fd.draw("B_to_D_LQ.pdf")


