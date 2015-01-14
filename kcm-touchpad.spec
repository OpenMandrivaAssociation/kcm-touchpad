%define release 2
%define git 20141125
Name:           kcm-touchpad
Version:        1.1
Summary:        Touchpad advanced configuration GUI for KDE
Release:        %{release}.%{git}
License:        GPLv2
Group:          Graphical desktop/KDE
URL:            https://projects.kde.org/projects/playground/utils/kcm-touchpad
# git clone git://anongit.kde.org/kcm-touchpad
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  kdelibs4-devel
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xorg-synaptics)
BuildRequires:	pkgconfig(xi)

Requires:       kdebase4-runtime

Conflicts:		kcm_touchpad

%description
KCM, daemon and applet for touchpad.

%files 
%doc COPYING README.md
%{_kde_bindir}/kcm-touchpad-list-devices
%{_kde_libdir}/kde4/kded_touchpad.so
%{_kde_libdir}/kde4/plasma_engine_touchpad.so
%{_kde_services}/kcm_touchpad.desktop
%{_kde_services}/plasma-applet-touchpad.desktop
%{_kde_services}/plasma-dataengine-touchpad.desktop
%{_kde_services}/kded/touchpad.desktop
%{_kde_appsdir}/desktoptheme/default/icons/touchpad.svg
%{_kde_appsdir}/kcm_touchpad/kcm_touchpad.notifyrc
%{_kde_appsdir}/plasma/plasmoids/touchpad/contents/ui/touchpad.qml
%{_kde_appsdir}/plasma/plasmoids/touchpad/metadata.desktop
%{_kde_appsdir}/plasma/services/touchpad.operations
%{_kde_datadir}/config.kcfg/touchpad.kcfg
%{_kde_datadir}/config.kcfg/touchpaddaemon.kcfg
%{_kde_iconsdir}/hicolor/*/devices/input-touchpad.png
%{_kde_iconsdir}/hicolor/scalable/devices/input-touchpad.svgz
%{_datadir}/dbus-1/interfaces/org.kde.touchpad.xml

#-----------------------------------------------------------------------------

%prep
%setup -qn %{name}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


