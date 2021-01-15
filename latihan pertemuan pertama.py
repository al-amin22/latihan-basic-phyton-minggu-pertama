#!/usr/bin/env python
# coding: utf-8

# In[7]:


#latihan no 1

nama = str(input("nama: "))

umur = int(input("umur: "))

tinggi = float(input("tinggi: "))

print("nama saya {}, umur saya  {} tahun, tinggi saya {}".format(nama, umur, tinggi))


# In[8]:


#latihan no 2

r = float(input("masukan jari-jari lingkaran: "))

phi = 22/7

luas = phi*r*r

print("luas lingkaran adalah:{} ".format(luas))


# In[ ]:


#latihan no 3

input_nilai_teori = int(input("masukan nilai teori anda: "))

input_nilai_praktek = int(input("masukan nilai praktek anda: "))

if (input_nilai_teori >= 70) and (input_nilai_praktek >= 70):
    print("selamat anda lulus")
    
elif (input_nilai_teori >= 70) and (input_nilai_praktek < 70):
    print("anda harus mengulang ujian praktek")
    
elif (input_nilai_teori < 70) and (input_nilai_praktek >= 70):
    print("anda harus mengulang ujian toeri")

elif (input_nilai_teori < 70) and (input_nilai_praktek < 70):
    print("anda harus mengulang ujian teori dan praktek")

