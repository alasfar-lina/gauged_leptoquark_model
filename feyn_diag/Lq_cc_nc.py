from pyfeyn.user import *

processOptions()
fd = FeynDiagram()
# up charged current 
# in2 = Point(-4,  2)
# in1 = Point(-4, -2)
# in_vtx = Vertex(-2, 0, mark=CIRCLE).addLabel(r"$-ig_{LQ}\,\mathcal{ U}_{q_u\nu}$",displace=-1.2)
# out_vtx = Vertex(1, 0)
# fa1 = Fermion(in1, in_vtx).addArrow().addLabel(r"\Pcharm,\Ptop",displace=+0.5)
# fa2 = Fermion(in_vtx, in2).addArrow().addLabel(r"\Pnum, \Pnut",displace=+0.5)

# bos = Photon(in_vtx, out_vtx).addLabel(r"$V^{+}$")
#down charged current
in2 = Point(-4,  2)
in1 = Point(-4, -2)
in_vtx = Vertex(-2, 0, mark=CIRCLE).addLabel(r"$-ig_{LQ}\,\mathcal{ U}^*_{q_d\ell}$",displace=-1.2)
out_vtx = Vertex(1, 0)
fa1 = Fermion(in1, in_vtx).addArrow().addLabel(r"\Pmu,\Ptau",displace=+0.5)
fa2 = Fermion(in_vtx, in2).addArrow().addLabel(r" \Pstrange ,\Pbottom ",displace=+0.5)

bos = Photon(in_vtx, out_vtx).addLabel(r"$V^{-}$")
# neutral current
# in2 = Point(-4,  2)
# in1 = Point(-4, -2)
# in_vtx = Vertex(-2, 0, mark=CIRCLE).addLabel(r"$-iX\frac{g_{LQ}}{c_{LQ}}$",displace=-1.2)
# out_vtx = Vertex(1, 0)
# fa1 = Fermion(in1, in_vtx).addArrow().addLabel(r"\Plepton,\Pquark",displace=+0.5)
# fa2 = Fermion(in_vtx, in2).addArrow().addLabel(r" \Plepton ,\Pquark ",displace=+0.5)

# bos = Photon(in_vtx, out_vtx).addLabel(r"$U^{0}$")

fd.draw("charged_current2.pdf")
