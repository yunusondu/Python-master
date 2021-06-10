from core.hyperoptic.hyperoptic import HyperOptic
from core.plusnet.plusnet import PlusNet

if __name__ == '__main__':
    '''  
  hyperoptic = HyperOptic()
     hyperoptic.get_broadband_only_deals()

    hyperoptic.driver.quit()
'''
    plusnet = PlusNet()
    plusnet.get_broadband_only_deals()
