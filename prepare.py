#!/usr/bin/env python3
import os
import sys
from platform import uname
from core import functions

if os.getuid() != 0:
    print("Sorry. This script requires root privileges, Switch to the root user and try again.")
    sys.exit()

os.system("clear")
obj = functions.Functions()


def main():
    try:
        print("""
            ██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗ ███████╗
            ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
            ██████╔╝██████╔╝█████╗  ██████╔╝███████║██████╔╝█████╗
            ██╔═══╝ ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██╔══██╗██╔══╝
            ██║     ██║  ██║███████╗██║     ██║  ██║██║  ██║███████╗
            ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
            """)
        print("\tPrepare\033[91m :: \033[0mA powerful tool for preparing your system!")
        print("\tCode\033[91m    :: \033[0mNaategh")
        print("\tVersion\033[91m :: \033[0m1.0")
        print("\tContact\033[91m :: \033[0mmanamtabeshekan@gmail.com")
        print("\n")
        print("\t\033[91m[~] Before using this script be sure your source list work as well!\n")
        print("\033[91m1) \033[0mupdate && upgrade\t\033[91m6) \033[0mGraphic")
        print("\033[91m2) \033[0mdist-upgrade\t\t\033[91m7) \033[0mUseful")
        print("\033[91m3) \033[0mProgramming\t\t\033[91m8) \033[0mSocial")
        print("\033[91m4) \033[0mOffice\t\t\033[91m9) \033[0mEtc")
        print("\033[91m5) \033[0mInternet\t\t\033[91m10) \033[0mHacking")
        print("")
        print("\033[91m99) \033[0mexit")
        choice = input("\n\033[36mEnter your choice: \033[0m")
        print("")

        while choice == '1':
            os.system("apt-get update && apt-get upgrade")
            main()

        while choice == '2':
            os.system("apt-get update && apt-get install -y upgrade")
            main()

        while choice == '3':
            obj.Programming()
            ide = input("\033[36mIde > \033[0m")
            if ide == '1':
                os.system(
                    "apt-get install -y apache2 && apt-get install -y php-pear php-fpm php-dev php-zip php-curl php-xmlrpc php-gd php-mysql php-mbstring php-xml libapache2-mod-php php7.0 libapache2-mod-php7.0 && apt-get install -y mysql-server && service apache2 start")
                print("")
            elif ide == '2':
                os.system(
                    'wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg |  apt-get-key add - && echo "deb https://download.sublimetext.com/ apt-get/stable/" |  tee /etc/apt-get/sources.list.d/sublime-text.list && apt-get update && apt-get install -y sublime-text')
                print("")
            elif ide == '3':
                os.system("add-apt-get-repository ppa:webupd8team/atom && apt-get update; apt-get install -y atom")
                print("")
            elif ide == '4':
                os.system(
                    'wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-get-key add - && sudo add-apt-get-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" && sudo apt-get install -y code')
                print("")
            elif ide == '5':
                os.system("apt-get install -y default-jdk && snap install eclipse --classic")
                obj.Programming()
            elif ide == '6':
                os.system(
                    "apt-get-add-repository ppa:maarten-fonville/android-studio && apt-get update && apt-get install -y android-studio")
                print("")
            elif ide == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '4':
            obj.Office()
            off = input("\033[36mOffice > \033[0m")
            if off == '1':
                os.system("apt-get install -y gedit")
                print("")
            elif off == '2':
                os.system(
                    "add-apt-get-repository ppa:libreoffice/ppa && apt-get update && apt-get install -y libreoffice")
            elif off == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '5':
            obj.Internet()
            browser = input("\033[36mBrowser > \033[0m")
            if browser == '1':
                sysType = uname()[4]
                if sysType == 'x86_64':
                    os.system(
                        "apt-get install -y libxss1 libappindicator1 libindicator7 && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome*.deb")
                elif sysType == "i686":
                    os.system(
                        "apt-get install -y libxss1 libappindicator1 libindicator7 && wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb && dpkg -i google-chrome*.deb")
                    print("")
            elif browser == '2':
                os.system(
                    "add-apt-get-repository ppa:mozillateam/firefox-next && apt-get update && apt-get install -y firefox")
                print("")
            elif browser == '3':
                os.system("apt-get install -y chromium-browser")
                print("")
            elif browser == '4':
                os.system(
                    "add-apt-get-repository ppa:webupd8team/tor-browser && apt-get update && apt-get install -y tor-browser")
                print("")
            elif browser == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '6':
            obj.Graphic()
            graphic = input("\033[36mGraphic > \033[0m")
            if graphic == '1':
                os.system(
                    "add-apt-get-repository ppa:otto-kesselgulasch/gimp-edge && apt-get update && sudo apt-get install -y gimp gimp-gmic")
                print("")
            elif graphic == '2':
                os.system(
                    "add-apt-get-repository ppa:inkscape.dev/stable && apt-get update && apt-get install -y inkscape")
                print("")
            elif graphic == '3':
                os.system("add-apt-get-repository ppa:kritalime/ppa && apt-get update && apt-get install -y krita")
                print("")
            elif graphic == '4':
                os.system(
                    "add-apt-get-repository ppa:achadwick/mypaint-testing && apt-get update && apt-get install -y mypaint mypaint-data-extras")
                print("")
            elif graphic == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '7':
            obj.Useful()
            use = input("\033[36mUseful > \033[0m")
            if use == '1':
                os.system('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -')
                print("")
            elif use == '2':
                os.system("apt-get install -y vlc")
                print("")
            elif use == '3':
                os.system(
                    "add-apt-get-repository ppa:ubuntu-wine/ppa && apt-get update && apt-get install -y wine1.8 winetricks")
                print("")
            elif use == '4':
                os.system(
                    "apt-get-add-repository ppa:remmina-ppa-team/remmina-next && apt-get update &&  apt-get install -y remmina remmina-plugin-rdp libfreerdp-plugins-standard")
                print("")
            elif use == '5':
                os.system(
                    "add-apt-get-repository ppa:maarten-baert/simplescreenrecorder && apt-get update && apt-get install -y simplescreenrecorder")
                print("")
            elif use == '6':
                os.system("wget https://release.gitkraken.com/linux/gitkraken-amd64.deb && dpkg -i gitkraken-amd64.deb")
                print("")
            elif use == '7':
                os.system("apt-get install git && git clone https://github.com/getlantern/lantern.git")
                print("")
            elif use == '8':
                os.system("apt-get install -y thunderbird")
                print("")
            elif use == '9':
                os.system("apt-get install -y ngrok-client")
                print("")
            elif use == '10':
                os.system("add-apt-get-repository ppa:noobslab/apps && apt-get update && apt-get install -y xdman")
                print("")
            elif use == '11':
                os.system(
                    "sudo add-apt-get-repository ppa:ubuntuhandbook1/audacity && apt-get update && apt-get install -y audacity")
                print("")
            elif use == '12':
                os.system("apt-get install -y pidgin")
                print("")
            elif use == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '8':
            obj.Social()
            special = input("\033[36mSpecial > \033[0m")
            if special == '1':
                os.system(
                    "add-apt-get-repository ppa:atareao/telegram && apt-get update && apt-get install -y telegram")
                print("")
            elif special == '2':
                os.system(
                    'echo "deb https://dl.bintray.com/aluxian/deb beta main" | tee -a /etc/apt-get/sources.list.d/whatsie.list && gpg --keyserver pool.sks-keyservers.net --recv-keys 1537994D && gpg --export --armor 1537994D |  apt-get-key add - && apt-get update &&  apt-get install -y whatsie')
                print("")
            elif special == '3':
                os.system(
                    'apt-get install -y apt-get-transport-https && apt-get install curl && curl https://repo.skype.com/data/SKYPE-GPG-KEY |  apt-get-key add - && echo "deb https://repo.skype.com/deb stable main" |  tee /etc/apt-get/sources.list.d/skypeforlinux.list && apt-get update && apt-get install -y skypeforlinux')
                print("")
            elif special == '4':
                os.system(
                    "sudo add-apt-get-repository ppa:adilson/experimental && apt-get update && apt-get install -y choqok")
                print("")
            elif special == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '9':
            obj.Etc()
            etc = input("\033[36mEtc > \033[0m")
            if etc == '1':
                os.system(
                    "sudo add-apt-get-repository ppa:cumulus-team/cumulus && apt-get update && apt-get install -y cumulus")
                print("")
            elif etc == '2':
                os.system("apt-get install -y kbackup")
                print("")
            elif etc == '3':
                os.system("apt-get install -y filezilla")
                print("")
            elif etc == '4':
                os.system("apt-get install -y dtrx")
                print("")
            elif etc == '5':
                os.system("apt-get install -y photorec")
                print("")
            elif etc == '6':
                os.system(
                    "sudo add-apt-get-repository ppa:morphis/anbox-support && apt-get install -y anbox-modules-dkms && sudo modprobe ashmem_linux && sudo modprobe binder_linux && sudo snap install --devmode --beta anbox")
                print("")
            elif etc == '7':
                os.system("apt-get install -y virtualbox ")
                print("")
            elif etc == '8':
                os.system("apt-get install -y cowsay")
                print("")
            elif etc == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '10':
            obj.Hacking()
            Hack = input("\033[36mHacking > \033[0m")
            if Hack == '1':
                os.system(
                    "apt-get install git && git clone https://LaNMaSteR53@bitbucket.org/LaNMaSteR53/recon-ng.git &&")
                print("")
            elif Hack == '2':
                os.system("apt-get install nmap")
                print("")
            elif Hack == '3':
                os.system("apt-get install python3-pip && pip install wafw00f")
                print("")
            elif Hack == '4':
                os.system("apt-get install nikto -y")
                print("")
            elif Hack == '5':
                os.system(
                    "apt-get install openjdk-8-jre && https://portswigger.net/burp/releases/download?product=community&version=1.7.36&type=linux")
                print("")
            elif Hack == '6':
                os.system("apt-get install git && git clone https://github.com/sqlmapproject/sqlmap.git")
                print("")
            elif Hack == '7':
                os.system(
                    "apt-get install git && git clone https://github.com/wpscanteam/wpscan.git && cd wpscan && bundle install --without test && cd ..")
                print("")
            elif Hack == '8':
                os.system("apt-get install git && git clone https://github.com/rezasp/joomscan.git")
                print("")
            elif Hack == '9':
                os.system("apt-get install git && git clone https://github.com/Dionach/CMSmap")
                print("")
            elif Hack == '10':
                os.system(
                    "wget 'http://downloads.sourceforge.net/project/dirbuster/DirBuster%20%28jar%20%2B%20lists%29/1.0-RC1/DirBuster-1.0-RC1.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fdirbuster%2Ffiles%2FDirBuster%2520%2528jar%2520%252B%2520lists%2529%2F1.0-RC1%2F&ts=1370262745&use_mirror=nchc' -O DirBuster-1.0-RC1.tar.bz2 && tar -xjvf DirBuster-1.0-RC1.tar.bz2 && mv DirBuster-1.0-RC1 DirBuster && rm DirBuster-1.0-RC1.tar.bz2")
                print("")
            elif Hack == '11':
                os.system("apt-get install git && git clone https://github.com/crunchsec/crunch.git")
                print("")
            elif Hack == '12':
                os.system("apt-get install git && git clone https://github.com/magnumripper/JohnTheRipper.git")
                print("")
            elif Hack == '13':
                os.system("add-apt-get-repository ppa:pi-rho/security && apt-get update && apt-get install hydra")
                print("")
            elif Hack == '14':
                os.system("apt-get install git && git clone https://github.com/hashcat/hashcat.git")
                print("")
            elif Hack == '15':
                os.system("pip install hashid")
                print("")
            elif Hack == '16':
                os.system("apt-get install aircrack-ng")
                print("")
            elif Hack == '17':
                os.system("https://github.com/wi-fi-analyzer/mdk3-master.git")
                print("")
            elif Hack == '18':
                os.system("apt-get install reaver")
                print("")
            elif Hack == '19':
                os.system("apt-get-get install -y armitage")
                print(
                    "apt-get install curl && curl -# -o /tmp/armitage.tgz http://www.fastandeasyhacking.com/download/armitage150813.tgz > /dev/null && tar -xvzf /tmp/armitage.tgz -C /opt > /dev/null && ln -s /opt/armitage/armitage /usr/local/bin/armitage > /dev/null && ln -s /opt/armitage/teamserver /usr/local/bin/teamserver > /dev/null && sh -c 'echo java -jar /opt/armitage/armitage.jar \$\* > /opt/armitage/armitage' > /dev/null && perl -pi -e 's/armitage.jar/\/opt\/armitage\/armitage.jar/g' /opt/armitage/teamserver > /dev/null")
            elif Hack == '20':
                os.system(
                    "apt-get install curl && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall && msfdb init")
                print("")
            elif Hack == '21':
                os.system(
                    "apt-get install ruby ruby-dev && apt-get install git && git clone https://github.com/beefproject/beef")
                print("")
            elif Hack == '22':
                os.system(
                    "apt-get install git && git clone https://github.com/offensive-security/exploitdb.git /opt/exploit-database && ln -sf /opt/exploit-database/searchsploit /usr/local/bin/searchsploit && cp -n /opt/exploit-database/.searchsploit_rc ~/")
                print("")
            elif Hack == '23':
                os.system("apt-get install git && git clone https://github.com/trustedsec/social-engineer-toolkit.git")
                print("")
            elif Hack == '24':
                os.system(
                    "apt-get install zlib1g zlib1g-dev && apt-get install build-essential && apt-get install ettercap")
                print("")
            elif Hack == '25':
                os.system("apt-get install macchanger")
                print("")
            elif Hack == '26':
                os.system(
                    "add-apt-get-repository ppa:wireshark-dev/stable && apt-get update && apt-get install wireshark")
                print("")
            elif Hack == '27':
                os.system("apt-get install sslstrip")
                print("")
            elif Hack == '28':
                os.system("https://github.com/epinna/weevely3.git")
                print("")
            elif Hack == '29':
                os.system("apt-get install proxychains")
                print("")
            elif Hack == '30':
                os.system("apt-get install git && git clone https://github.com/secretsquirrel/the-backdoor-factory.git")
                print("")
            elif Hack == '99':
                main()
            else:
                print("\n\033[91mWrong Command!\n")

        while choice == '99':
            print("---------- bye! ----------")
            sys.exit()

        allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '99']
        if choice not in allowed:
            main()

    except KeyboardInterrupt:
        print("\033[91mShutdown...\n\033[0m")
        sys.exit()


if __name__ == '__main__':
    main()
