%define name 	qmidiarp
%define version 0.0.2
%define release %mkrel 3

Summary: 	Simple, graphical MIDI arpeggiator
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://alsamodular.sourceforge.net/
License: 	GPL
Group: 		Sound
Source: 	%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	libalsa-devel qt3-devel

%description
QMidiArp can run several arpeggiators at the same time, both 
monophonically and with chords. It is based on user definable patterns 
where the indices 0..9 address the notes currently played on a keyboard.
Several other tokens define tempo, note length, velocity,...

%prep
%setup -q
perl -p -i -e "s/\-O2/$RPM_OPT_FLAGS/g" Makefile
perl -pi -e 's/QT_BASE_DIR\)\/lib/QT_BASE_DIR\)\/%{_lib}/g' Makefile
perl -pi -e 's/usr\/%{_lib}/usr\/%{_lib}/g' Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QMidiArp
Comment=MIDI Arpeggiator
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Midi;
Encoding=UTF-8
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%update_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README *.qma
%_bindir/%name
%{_datadir}/applications/mandriva-%{name}.desktop

