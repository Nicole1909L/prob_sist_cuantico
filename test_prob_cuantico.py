import prob_cuantico as ct
import unittest

class TestProvSistEstados (unittest.TestCase):

    def test_prob_sist_linea(self):
        result = ct.prob_sist_linea(vect=[2+1j,-3j,4],pos=1)
        self.assertAlmostEqual(result, 0.3)
        
        result = ct.prob_sist_linea(vect=[3+5j,6+3j,1],pos=2)
        self.assertAlmostEqual(result, 0.0125)
    
    def test_amplitud_trans(self):
        result = ct.amplitud_trans(v1=[2+1j,-3j,4],v2=[3+5j,6+3j,1])
        self.assertAlmostEqual(result,0.12247448713915893-0.5103103630798287j)
        
        result = ct.amplitud_trans(v1=[3+8j,1j,1],v2=[5j,6,2-1j])
        self.assertAlmostEqual(result,0.596962005795709-0.11370704872299219j)