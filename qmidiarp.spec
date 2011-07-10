%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define git_snapshot git20101211
%endif

Name:           qmidiarp
Summary:        Arpgeggiator, sequencer and LFO for ALSA
Version:        0.4.2
%if %branch
Release:        %mkrel -c %git_snapshot 1
%else
Release:        %mkrel 1
%endif
%if %branch
Source:         http://dl.sf.net/%{name}/%{name}-%{version}.%{git_snapshot}.tar.bz2
%else
Source:         http://dl.sf.net/%{name}/%{version}/%{name}-%{version}.tar.bz2
%endif
URL:            http://qmidiarp.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  alsa-lib-devel qt4-devel jackit-devel
BuildRequires:  desktop-file-utils

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

desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/qmidiarp.svg
%docdir %{_mandir}/man1/*
%{_mandir}/man1/*
%{_mandir}/de/man1/*
%{_mandir}/fr/man1/*
%{_datadir}/applications/%{name}.desktop

%changelog
