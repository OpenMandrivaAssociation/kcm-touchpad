%define git 20141125

Summary:	Advanced touchpad configuration GUI for KDE
Name:		kcm-touchpad
Version:	1.1
Release:	3.%{git}.4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/playground/utils/kcm-touchpad
# git clone git://anongit.kde.org/kcm-touchpad
Source0:	%{name}-%{version}-%{git}.tar.bz2
Source1:	kcm-touchpad_ru.tar.bz2
Patch0:		kcm-touchpad-1.1-lang.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-record)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-synaptics)
BuildRequires:	pkgconfig(xi)
Requires:	kdebase4-runtime
Conflicts:	kcm_touchpad
Obsoletes:	kcm_touchpad < 1.1

%description
Advanced touchpad configuration GUI for KDE.

%files -f kcm_touchpad.lang
%doc COPYING README.md
%{_kde_bindir}/kcm-touchpad-list-devices
%{_kde_libdir}/kde4/kded_touchpad.so
%{_kde_services}/kcm_touchpad.desktop
%{_kde_services}/kded/touchpad.desktop
%{_kde_appsdir}/kcm_touchpad/kcm_touchpad.notifyrc
%{_kde_datadir}/config.kcfg/touchpad.kcfg
%{_kde_datadir}/config.kcfg/touchpaddaemon.kcfg
%{_kde_iconsdir}/hicolor/*/devices/input-touchpad.png
%{_kde_iconsdir}/hicolor/scalable/devices/input-touchpad.svgz
%{_datadir}/dbus-1/interfaces/org.kde.touchpad.xml

#----------------------------------------------------------------------------

%package -n plasma-applet-touchpad
Summary:	Plasma applet to show current touchpad state
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
Conflicts:	%{name} < 1.1-3

%description -n plasma-applet-touchpad
Plasma applet to show current touchpad state.

%files -n plasma-applet-touchpad -f plasma_applet_touchpad.lang
%{_kde_appsdir}/desktoptheme/default/icons/touchpad.svg
%{_kde_appsdir}/plasma/plasmoids/touchpad/contents/ui/touchpad.qml
%{_kde_appsdir}/plasma/plasmoids/touchpad/metadata.desktop
%{_kde_appsdir}/plasma/services/touchpad.operations
%{_kde_libdir}/kde4/plasma_engine_touchpad.so
%{_kde_services}/plasma-applet-touchpad.desktop
%{_kde_services}/plasma-dataengine-touchpad.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-%{git}
%patch0 -p1

pushd po
tar -xvf %{SOURCE1}
popd

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang kcm_touchpad

%find_lang plasma_applet_touchpad
