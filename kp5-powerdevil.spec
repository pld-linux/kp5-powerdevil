#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.6
%define		qtver		5.15.2
%define		kpname		powerdevil

Summary:	Manages the power consumption settings of a Plasma Shell
Name:		kp5-%{kpname}
Version:	5.27.6
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	02d748a0b7395084a33c95201727bb02
URL:		https://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-bluez-qt-devel
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
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-networkmanager-qt-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	kp5-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	libxcb-devel
BuildRequires:	ninja
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
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

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
%attr(755,root,root) %{_libexecdir}/kauth/backlighthelper
%attr(755,root,root) %{_libexecdir}/kauth/discretegpuhelper
%ghost %{_libdir}/libpowerdevilconfigcommonprivate.so.5
%attr(755,root,root) %{_libdir}/libpowerdevilconfigcommonprivate.so.*.*.*
%ghost  %{_libdir}/libpowerdevilcore.so.2
%attr(755,root,root) %{_libdir}/libpowerdevilcore.so.*.*.*
%ghost  %{_libdir}/libpowerdevilui.so.5
%attr(755,root,root) %{_libdir}/libpowerdevilui.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilbrightnesscontrolaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevildimdisplayaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevildpmsaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilhandlebuttoneventsaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilkeyboardbrightnesscontrolaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilrunscriptaction_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/powerdevilsuspendsessionaction_config.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_datadir}/knotifications5/powerdevil.notifyrc
%{_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
/etc/xdg/autostart/powerdevil.desktop
%{_libdir}/libpowerdevilconfigcommonprivate.so
%{_libdir}/libpowerdevilcore.so
%{_libdir}/libpowerdevilui.so
%dir %{_libdir}/qt5/plugins/kf5/powerdevil
%{_libdir}/qt5/plugins/kf5/powerdevil/powerdevilupowerbackend.so
%{_libdir}/qt5/plugins/powerdevilwirelesspowersavingaction_config.so
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_datadir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.discretegpuhelper.conf
%{systemduserunitdir}/plasma-powerdevil.service
%attr(755,root,root) %{_prefix}/libexec/kauth/chargethresholdhelper
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
%{_datadir}/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
%{_datadir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_datadir}/qlogging-categories5/powerdevil.categories
%{_libdir}/qt5/plugins/powerdevilpowerprofileaction_config.so

%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilactivitiesconfig.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilglobalconfig.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilprofilesconfig.so
%dir %{_libdir}/qt5/plugins/powerdevil
%dir %{_libdir}/qt5/plugins/powerdevil/action
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_brightnesscontrolaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_dimdisplayaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_dpmsaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_handlebuttoneventsaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_powerprofileaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_runscriptaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_suspendsessionaction.so
%{_libdir}/qt5/plugins/powerdevil/action/powerdevil_wirelesspowersavingaction.so
%{_desktopdir}/kcm_powerdevilactivitiesconfig.desktop
%{_desktopdir}/kcm_powerdevilglobalconfig.desktop
%{_desktopdir}/kcm_powerdevilprofilesconfig.desktop
