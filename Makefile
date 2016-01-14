all:

install:
	install -D -m 644 conf/60-n9-n950-ui.conf $(DESTDIR)/var/lib/environment/compositor/60-n9-n950-ui.conf
	install -D -m 644 conf/61-nemo-mobile-hw-wayland.conf $(DESTDIR)/var/lib/environment/nemo/61-nemo-mobile-hw-wayland.conf
	install -D -m 644 conf/powervr.ini $(DESTDIR)/etc/powervr.ini
	install -D -m 644 prjconf/n950-n9-prjconf.xml $(DESTDIR)/usr/share/prjconf/n950-n9-prjconf.xml
	install -D -m 644 conf/plugins.conf $(DESTDIR)/var/lib/environment/ofono/plugins.conf
	install -D -m 644 conf/camera-pipelines.conf $(DESTDIR)/etc/camera/pipelines.conf
	install -D -m 644 conf/RM-680_Himalaya_AUO_V1_1.raw $(DESTDIR)/lib/firmware/RM-680_Himalaya_AUO_V1_1.raw
	install -D -m 644 conf/RM-696_Pyrenees_SMD_V1_6.raw $(DESTDIR)/lib/firmware/RM-696_Pyrenees_SMD_V1_6.raw
