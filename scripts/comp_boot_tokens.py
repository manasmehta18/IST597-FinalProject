import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cos


tokens1 = np.zeros((5, 1280))
tokens2 = np.zeros((5, 1280))

token_sim = np.zeros(25)


for i in range(5):
    token1 = np.load("../outputs/tokens/constable__" + str(i) + ".npy")
    token_mean1 = np.mean(token1, axis=0).reshape(1,-1)
    tokens1[i,:] = token_mean1

    token2 = np.load("../outputs/tokens/va__" + str(i) + ".npy")
    token_mean2 = np.mean(token2, axis=0).reshape(1,-1)
    tokens2[i,:] =  token_mean2

n = 0

for token1 in tokens1:
    for token2 in tokens2:    
        token_sim[n] = cos(token1.reshape(1,-1), token2.reshape(1,-1))
        n += 1


print(token_sim)
print(np.mean(token_sim)) # mean = 0.9690051293422417
print(np.std(token_sim)) # std dev = 0.00772387118664006

# next steps: remove non-sky areas (focus on clouds) - instead of blacking out pixels - crop images 


############### OLD VALUES ###################### (constable-lionel)
# mean = 0.9700518231736659
# std dev = 0.009405679132623376

# [0.97695837 0.97334154 0.97803321 0.97638162 0.971577   0.97683256
#  0.97408801 0.97724295 0.97662705 0.97141546 0.95140888 0.95240524
#  0.95496489 0.95730458 0.94786307 0.97114448 0.96742349 0.97216208
#  0.97258127 0.9648924  0.97914297 0.97424604 0.98121126 0.97758849
#  0.97445866]


############### OLD VALUES ###################### (constable-valenciennes)

# mean = 0.9611646958242437
# std dev = 0.006036362043426713

# [0.96831273 0.96363712 0.96915874 0.96842101 0.96685905 0.96612947
#  0.96182865 0.96607044 0.96516301 0.96460889 0.95097762 0.94423672
#  0.95073149 0.95390027 0.95432104 0.96230228 0.95854126 0.96149154
#  0.96323203 0.96120175 0.96416681 0.96017298 0.96327957 0.9602612
#  0.96011172]


############### NEW NEW VALUES ###################### (constable-lionel)

# mean = 0.9690051293422417
# std dev = 0.00772387118664006

# [0.96036023 0.97000714 0.95947838 0.97776835 0.97058673 0.96848831
#  0.96975627 0.96396907 0.9845367  0.9786136  0.95664677 0.9637877
#  0.95777521 0.97105855 0.96460317 0.96268212 0.97064638 0.96122975
#  0.97918775 0.97340088 0.96940265 0.96565391 0.96428144 0.98430298
#  0.9769042 ]

############### NEW NEW VALUES ###################### (constable-valenciennes)

# mean = 0.9759539905761057
# std dev = 0.005967243521986409

# [0.98420831 0.97633959 0.98162606 0.96702271 0.9834628  0.97493078
#  0.9811281  0.97612816 0.97247949 0.97487734 0.97699235 0.96993022
#  0.97662485 0.95943009 0.97852205 0.98253709 0.98023312 0.98113882
#  0.96898088 0.98509744 0.97244134 0.97807959 0.97338457 0.96903812
#  0.97421589]

############### NEW VALUES ###################### (constable-lionel)

# mean = 0.9586974934631368
# std dev = 0.009633718443488464

# [0.95599883 0.95988038 0.95610653 0.9574109  0.94488411 0.95552516
#  0.95537633 0.96007494 0.95902321 0.93084203 0.97398323 0.97398146
#  0.96932216 0.96038009 0.95553302 0.96647536 0.96978745 0.97034705
#  0.96705551 0.94282403 0.96416213 0.96685391 0.96414115 0.95481054
#  0.95203148 0.96705483 0.96265438 0.96663282 0.95760076 0.93557351
#  0.96686559 0.96626488 0.95868522 0.95778544 0.95136728 0.95678853
#  0.95848553 0.96059213 0.95896086 0.93865097 0.97113061 0.96979149
#  0.96601958 0.95342437 0.95536558 0.96728768 0.96560977 0.96745763
#  0.96051872 0.94075828 0.97093138 0.97014459 0.96247752 0.96473508
#  0.9568746  0.96274211 0.96355899 0.96698459 0.96464267 0.94401953
#  0.97142397 0.9724218  0.96704133 0.96844097 0.95652527 0.9642477
#  0.96744018 0.96939394 0.96980438 0.94810683 0.96879163 0.96176438
#  0.95438176 0.9511728  0.94819773 0.95171085 0.96541751 0.95069339
#  0.9560013  0.94094683 0.96063339 0.96095188 0.96370379 0.95275654
#  0.95102836 0.96335953 0.95839277 0.96508053 0.95596614 0.93642994
#  0.95290501 0.95502098 0.95605798 0.94884991 0.94353811 0.9548473
#  0.95061292 0.96011113 0.95424817 0.92608195]



############### NEW VALUES ###################### (constable-valenciennes)

# mean = 0.9606675857415516
# std dev = 0.010911637172294137

# [0.96447765 0.97238962 0.96499465 0.96891162 0.96736153 0.95790564
#  0.94821646 0.93700188 0.96577802 0.94179976 0.96662064 0.97035462
#  0.97141688 0.97145801 0.97110813 0.96989384 0.95845655 0.94367271
#  0.96720374 0.94624009 0.96928667 0.97157631 0.96968341 0.97123843
#  0.96938063 0.97062495 0.9578416  0.94092234 0.96730209 0.94428891
#  0.95654222 0.96861561 0.96604526 0.96820724 0.96787613 0.95819563
#  0.9537025  0.93850805 0.96758993 0.93917608 0.96770104 0.96947885
#  0.96822106 0.96700673 0.96723342 0.96867803 0.95894002 0.93977152
#  0.9660472  0.94378403 0.9608882  0.9711755  0.97017919 0.9725008
#  0.97184621 0.96334355 0.96168688 0.94596264 0.97083783 0.9461359
#  0.96308378 0.97362751 0.97217728 0.97506495 0.9752335  0.96460456
#  0.95887308 0.94823363 0.97161031 0.95042345 0.95869428 0.95963049
#  0.96224731 0.95946021 0.96366782 0.95951583 0.96483553 0.9371055
#  0.96065473 0.94039582 0.9665965  0.96780778 0.96385483 0.96605484
#  0.96426494 0.96562852 0.95067834 0.94025305 0.96251724 0.94252659
#  0.96441067 0.9695571  0.96213381 0.96463346 0.96478252 0.96029281
#  0.94570935 0.9331307  0.96192167 0.93757966]

######## sky paintings #########

# constable - constable: 1.0000004
# constable - lionel: 0.97206795
# constable - va: 0.94715333
# constable - boudin: 0.96267784
# constable - watts: 0.95839983
# constable - cox: 0.93659633
# constable - lee: 0.9390787


############### OLD VALUES ###################### (constable-lionel)
# mean = 0.9683950542502991
# std dev = 0.011560518942807983

# [0.97695837 0.97334154 0.97803321 0.97638162 0.971577   0.97910268
#  0.98116147 0.98131923 0.9750306  0.98107002 0.97683256 0.97408801
#  0.97724295 0.97662705 0.97141546 0.97988876 0.97546284 0.98084132
#  0.97382472 0.98384482 0.95140888 0.95240524 0.95496489 0.95730458
#  0.94786307 0.95676451 0.95543273 0.95755805 0.95233151 0.96062479
#  0.97114448 0.96742349 0.97216208 0.97258127 0.9648924  0.97331905
#  0.97002586 0.97743298 0.96925543 0.9812916  0.97914297 0.97424604
#  0.98121126 0.97758849 0.97445866 0.97967925 0.97581274 0.98160887
#  0.97624807 0.98269958 0.94499794 0.94432487 0.94732264 0.94852633
#  0.94253889 0.9520789  0.95387435 0.94977575 0.94977209 0.95236877
#  0.95131738 0.94914894 0.95245362 0.95504722 0.94701164 0.95698565
#  0.95863893 0.95509482 0.95557677 0.95708259 0.97729999 0.97176152
#  0.9780371  0.97782187 0.97018063 0.97734554 0.97146184 0.98093776
#  0.97329514 0.98394667 0.9684102  0.96289469 0.96966348 0.97201522
#  0.96011663 0.97102652 0.96595019 0.97607272 0.9661891  0.978955
#  0.97619171 0.97337455 0.97707156 0.97665792 0.97260759 0.97862481
#  0.9774569  0.97995468 0.97583455 0.98148425]

# constable - constable: 1.0000002
# constable - lionel: 0.96817565
# constable - va: 0.95588243
# constable - boudin: 0.95225775
# constable - watts: 0.96759415
# constable - cox: 0.94594586
# constable - lee: 0.95053077

# constable - gogh: 0.93010426
# constable - landscape: 0.91335917
# constable - sketch: 0.9056036
# constable - images: 0.898628                       
# gogh - landscape: 0.8923956
# va - landscape: 0.91201454

# new - bootstrap sampling
# TODO: picasso

# issues: smoothing due to averages, learning content, metric, more artists  

