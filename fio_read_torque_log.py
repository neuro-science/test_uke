#!/usr/bin/env python3
#def fio_read_torque_log(fp, fi, fo): 

# fp = '/home/pwang/Dropbox/codes/6PD/3pro1_3/jobs/'
# fi = '505730.torquemaster.neurophys.uke.uni-hamburg.de.out'
# fo = 'test.dat'

# =============================================================================
# #read all text file, seems not easy
# file_object = open(''.join((fp, fi)), 'r') 
# try:
#     data = file_object.read() 
# finally:
#     file_object.close()
# print(data)
# print(len(data))
# import re
# print (re.findall('\d+', data ))
# =============================================================================

 # read line by line -- it works
# fin = open(''.join((fp, fi)), 'r') 
# fout = open(''.join((fp, fo)), 'a') 
# for line in fin:    
#      if line[0:4] == 'Hx =':
#          print(line[4:], end='')
#          fout.write(line[4:])
# fin.close()
# fout.close()
# print("Done!")

### merge two files
# fin = open('/mnt/homes/home020/pwang/6PD/3sum/36clusters/coh_rn_th2.0+2.0+1.3_nh5.txt', 'r') 
# fout = open('/mnt/homes/home020/pwang/6PD/3sum/36clusters/coh_rn_th2.0+2.0+1.3_nh5.dat', 'w') 

# for line in fin:    
#      if line[0:3] == 'Hx[':
#          print(line[7:18], end='\n')
#          fout.write(''.join((line[7:18], '\n')))
# fin.close()
# fout.close()

# fin = open('/mnt/homes/home020/pwang/6PD/3sum/36clusters/coh2_rn_th2.0+2.0+1.3_nh5.txt', 'r') 
# fout = open('/mnt/homes/home020/pwang/6PD/3sum/36clusters/coh_rn_th2.0+2.0+1.3_nh5.dat', 'a') 

# for line in fin:    
#      if line[0:3] == 'Hx[':
#          print(line[7:18], end='\n')
#          fout.write(''.join((line[7:18], '\n')))
# fin.close()
# fout.close()
# print("Done!")

#one file again
fin = open('/mnt/homes/home020/pwang/share/jobs/514427.out', 'r') 
fout = open('/mnt/homes/home020/pwang/6PD/3sum/36clusters/coh_rn_th2.0+2.0+1.3_nh3.dat', 'w') 

for line in fin:    
     if line[0:3] == 'Hx[':
         print(line[7:18], end='\n')
         fout.write(''.join((line[7:18], '\n')))
fin.close()
fout.close()
print("Done!")
