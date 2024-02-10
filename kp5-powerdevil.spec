#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.93.0
%define		qtver		5.15.2
%define		kpname		powerdevil

Summary:	Manages the power consumption settings of a Plasma Shell
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	1b0d03debe19a91ea0289010d16f994f
URL:		https://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf6-bluez-qt-devel
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kcmutils-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kglobalaccel-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kidletime-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-kirigami-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-knotifyconfig-devel
BuildRequires:	kf6-networkmanager-qt-devel
BuildRequires:	kf6-solid-devel
BuildRequires:	kp5-kwayland-devel
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	kp5-plasma-activities-devel
BuildRequires:	kp5-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Manages the power consumption settings of a Plasma Shell.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/org_kde_powerdevil
%ghost  %{_libdir}/libpowerdevilcore.so.2
%attr(755,root,root) %{_libdir}/libpowerdevilcore.so.*.*.*
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
/etc/xdg/autostart/powerdevil.desktop
%{_libdir}/libpowerdevilconfigcommonprivate.so
%{_libdir}/libpowerdevilcore.so
%dir %{_libdir}/qt6/plugins/kf6/powerdevil
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/powerdevil/powerdevilupowerbackend.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
%{systemduserunitdir}/plasma-powerdevil.service
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
%{_datadir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy

%dir %{_libdir}/qt6/plugins/powerdevil
%dir %{_libdir}/qt6/plugins/powerdevil/action
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_brightnesscontrolaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_dimdisplayaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_dpmsaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_handlebuttoneventsaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_powerprofileaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_runscriptaction.so
%attr(755,root,root) %{_libdir}/qt6/plugins/powerdevil/action/powerdevil_suspendsessionaction.so

%{systemduserunitdir}/plasma-powerprofile-osd.service
%attr(755,root,root) %{_libdir}/libpowerdevilconfigcommonprivate.so.*.*
%ghost %{_libdir}/libpowerdevilconfigcommonprivate.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/backlighthelper
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/chargethresholdhelper
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/discretegpuhelper
%attr(755,root,root) %{_prefix}/libexec/power_profile_osd_service
%{_desktopdir}/kcm_powerdevilprofilesconfig.desktop
%{_datadir}/dbus-1/services/org.kde.powerdevil.powerProfileOsdService.service
%{_datadir}/qlogging-categories6/powerdevil.categories
