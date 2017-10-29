%define		kdeplasmaver	5.11.2
%define		qtver		5.3.2
%define		kpname		powerdevil

Summary:	Manages the power consumption settings of a Plasma Shell
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	4cbc031a4ee77b9c6fb31cb79f8902c6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kidletime-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	kp5-plasma-workspace
BuildRequires:	libxcb-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Manages the power consumption settings of a Plasma Shell.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
/etc/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%attr(755,root,root) %{_libdir}/kauth/backlighthelper
%attr(755,root,root) %ghost %{_libdir}/libpowerdevilconfigcommonprivate.so.5
%attr(755,root,root) %{_libdir}/libpowerdevilconfigcommonprivate.so.*.*.*
%attr(755,root,root) %ghost  %{_libdir}/libpowerdevilcore.so.2
%attr(755,root,root) %{_libdir}/libpowerdevilcore.so.*.*.*
%attr(755,root,root) %ghost  %{_libdir}/libpowerdevilui.so.5
%attr(755,root,root) %{_libdir}/libpowerdevilui.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_powerdevilactivitiesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_powerdevilglobalconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_powerdevilprofilesconfig.so
#%attr(755,root,root) %{_libdir}/qt5/plugins/kded_powerdevil.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilbrightnesscontrolaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevildimdisplayaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevildpmsaction.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevildpmsaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilhandlebuttoneventsaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilkeyboardbrightnesscontrolaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilrunscriptaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilsuspendsessionaction_config.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_datadir}/knotifications5/powerdevil.notifyrc
#%{_datadir}/kservices5/kded/powerdevil.desktop
%{_datadir}/kservices5/powerdevil*.desktop
%{_datadir}/kservicetypes5/powerdevilaction.desktop
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy

/etc/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
/etc/xdg/autostart/powerdevil.desktop
%{_libdir}/kauth/discretegpuhelper
%{_libdir}/libpowerdevilconfigcommonprivate.so
%{_libdir}/libpowerdevilcore.so
%{_libdir}/libpowerdevilui.so
%{_libdir}/org_kde_powerdevil
%dir %{_libdir}/qt5/plugins/kf5/powerdevil
%{_libdir}/qt5/plugins/kf5/powerdevil/powerdevilupowerbackend.so
%{_libdir}/qt5/plugins/powerdevilwirelesspowersavingaction_config.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
