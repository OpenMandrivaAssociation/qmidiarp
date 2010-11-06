%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define cvs_snapshot cvs20101101
%endif

Name:           qmidiarp
Summary:        Arpgeggiator, sequencer and LFO for ALSA
Version:        0.0.3
%if %branch
Release: 		%mkrel -c %cvs_snapshot 1
%else
Release: 		%mkrel 1
%endif
%if %branch
Source:         http://dl.sf.net/alsamodular/%{name}-%{version}.%{cvs_snapshot}.tar.bz2
%else
Source:         http://dl.sf.net/alsamodular/%{name}-%{version}.tar.bz2
%endif
URL:            http://alsamodular.sourceforge.net/
License:        GPLv2
Group:          Applications/Multimedia
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
BuildRequires:  alsa-lib-devel qt4-devel jackit-devel

%description
Advanced arpgeggiator, step sequencer and MIDI LFO for the ALSA sequencer.

%prep 
%setup -q

%if %mdkversion < 201000
iconv -f=utf8 -t=latin1 man/de/%{name}.1 -o man/de/%{name}.1
iconv -f=utf8 -t=latin1 man/fr/%{name}.1 -o man/fr/%{name}.1
%endif

%build 
%configure 
%make
%install
rm -rf %{buildroot}
%makeinstall_std

%{__mkdir} -p %{buildroot}%{_datadir}/pixmaps
%{__install} -m 0644 src/pixmaps/qmidiarp2.xpm %{buildroot}%{_datadir}/pixmaps

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QMidiArp
Comment=Arpeggiator Sequencer LFO
Exec=%{_bindir}/%{name}
Icon=qmidiarp2
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
Encoding=UTF-8
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/qmidiarp2.xpm
%docdir %{_mandir}/man1/*
%{_mandir}/man1/*
%{_mandir}/de/man1/*
%{_mandir}/fr/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop

%changelog
