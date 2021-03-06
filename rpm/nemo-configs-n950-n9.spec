Name:       nemo-configs-n950-n9
Summary:    Some configs for n9/n950 adaptations
Version:    1
Release:    1
Group:      Configs
License:    GPLv2
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: oneshot
BuildRequires: repomd-pattern-builder
Requires:   oneshot
%{_oneshot_requires_post}

%description
%{summary}.

# Set the provides for package-groups/project-config once it's ready to replace old configuration packages
%package -n n950-n9-patterns
Summary:    Repository patterns for n950/n9 hw
#Provides:   package-groups

%description -n n950-n9-patterns
%{summary}.

%package -n n950-n9-prjconf
Summary:    Project configs for n950/n9 hw repos for OBS
#Provides:   project-config

%description -n n950-n9-prjconf
%{summary}.

%package wayland
Summary:    Configuration files for n950/n9 wayland env
Obsoletes:  ti-omap3-sgx-configs-default <= 1.4.268.5
Provides:   ti-omap3-sgx-configs-default > 1.4.268.5
Provides:   ti-omap3-sgx-configs
Requires:   kernel-adaptation-n950 >= 3.5.3.20141127.1

%description wayland
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
make

%post
%{_oneshotdir}/sensord-daemon-conf-setup
%{_bindir}/add-oneshot --late sensord-daemon-conf-setup

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} ONESHOTDIR=%{_oneshotdir} install
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system/basic.target.wants/
/usr/bin/repomd-pattern-builder.py --patternxml -p ./patterns/ -o %{buildroot}/usr/share/package-groups/ --version=%{version} --release=%{release}

%files
%defattr(-,root,root,-)
/var/lib/environment/ofono/plugins.conf
%{_sysconfdir}/camera/pipelines.conf
/lib/firmware/RM-680_Himalaya_AUO_V1_1.raw
/lib/firmware/RM-696_Pyrenees_SMD_V1_6.raw
%attr(755, root, root) %{_oneshotdir}/sensord-daemon-conf-setup
%{_sysconfdir}/sensorfw/sensord.conf.d/sensord-rm_680.conf
%{_sysconfdir}/sensorfw/sensord.conf.d/sensord-rm_696.conf
%{_sysconfdir}/xdg/QtProject/Sensors.conf

%files -n n950-n9-patterns
%defattr(-,root,root,-)
%{_datadir}/package-groups/*.xml

%files -n n950-n9-prjconf
%defattr(-,root,root,-)
%{_datadir}/prjconf/*.xml

%files wayland
%{_sysconfdir}/powervr.ini
/var/lib/environment/compositor/60-n9-n950-ui.conf
/var/lib/environment/nemo/61-nemo-mobile-hw-wayland.conf
