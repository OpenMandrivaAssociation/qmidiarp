%global	_enable_debug_packages %{nil}

Summary:	Arpgeggiator, sequencer and LFO for JACK and ALSA
Name:	qmidiarp
Version:	0.7.1
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://qmidiarp.sourceforge.net/
Source0:	https://sourceforge.net/projects/qmidiarp/files/qmidiarp/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:		cmake >= 3.10
BuildRequires:		cmake(Qt5LinguistTools)
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(cairo)
BuildRequires:		pkgconfig(gl)
BuildRequires:		pkgconfig(glu)
BuildRequires:		pkgconfig(jack)
BuildRequires:		pkgconfig(liblo)
BuildRequires:		pkgconfig(lv2)
BuildRequires:		pkgconfig(pango)
BuildRequires:		pkgconfig(pangocairo)
BuildRequires:		pkgconfig(Qt5Core)
BuildRequires:		pkgconfig(Qt5Gui)
BuildRequires:		pkgconfig(Qt5Widgets)
BuildRequires:		pkgconfig(Qt5Xml)

%description
Advanced arpgeggiator, step sequencer and MIDI LFO for JACK and ALSA.

%files -f %{name}.lang
%doc README NEWS COPYING AUTHORS
%{_bindir}/%{name}
%{_libdir}/lv2/%{name}*.lv2/*.so
%{_libdir}/lv2/%{name}*.lv2/*.ttl
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

# Fix lv2 plugins path
sed -i -e "s,/lib/lv2,/%{_lib}/lv2,g" CMakeLists.txt


%build
%cmake -DCONFIG_LV2_UI_RTK=1 \
				-DCONFIG_TRANSLATIONS=1

%make_build


%install
%make_install -C build

%find_lang %{name} --with-man
