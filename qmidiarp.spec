%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define git_snapshot git20101211
%endif

Name:           qmidiarp
Summary:        Arpgeggiator, sequencer and LFO for JACK and ALSA
Version:        0.5.1
%if %branch
Release:        %git_snapshot
%else
Release:        1
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
BuildRequires:  libalsa-devel qt4-devel jackit-devel
BuildRequires:  desktop-file-utils

%description
Advanced arpgeggiator, step sequencer and MIDI LFO for JACK and ALSA.

%prep
%setup -q

%build
%configure
%make
%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-man

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/qmidiarp.svg
%docdir %{_mandir}/man1/*
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop



%changelog
* Sat Mar 24 2012 Frank Kober <emuse@mandriva.org> 0.5.0-1
+ Revision: 786562
- new version 0.5.0

* Sun Jan 22 2012 Frank Kober <emuse@mandriva.org> 0.4.5-1
+ Revision: 765838
- new version 0.4.5

* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 0.4.4-2
+ Revision: 745040
- update description and correct tarball

* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 0.4.4-1
+ Revision: 744991
- new version 0.4.4
  o use find_lang macro
  o remove patch applied upstream
  o update summary

* Wed Dec 07 2011 Frank Kober <emuse@mandriva.org> 0.4.3-2
+ Revision: 738744
- add upstream bugfix patch

* Sun Nov 20 2011 Frank Kober <emuse@mandriva.org> 0.4.3-1
+ Revision: 732089
- new version 0.4.3

* Sun Jul 10 2011 Frank Kober <emuse@mandriva.org> 0.4.2-1
+ Revision: 689423
- new version 0.4.2

* Fri Jun 03 2011 Frank Kober <emuse@mandriva.org> 0.4.1-2
+ Revision: 682625
- upstream patch with bugfixes added

* Sun May 29 2011 Frank Kober <emuse@mandriva.org> 0.4.1-1
+ Revision: 681620
- new version 0.4.1

* Wed Jan 05 2011 Frank Kober <emuse@mandriva.org> 0.3.9-1mdv2011.0
+ Revision: 628899
- new version 0.3.9

* Sat Dec 11 2010 Frank Kober <emuse@mandriva.org> 0.0.3-0.cvs20101211.1mdv2011.0
+ Revision: 620580
- new cvs snapshot

* Sun Nov 28 2010 Frank Kober <emuse@mandriva.org> 0.0.3-0.cvs20101128.1mdv2011.0
+ Revision: 602363
- new cvs snapshot

* Sat Nov 06 2010 Frank Kober <emuse@mandriva.org> 0.0.3-0.cvs20101101.1mdv2011.0
+ Revision: 594229
- fix rpm group tag
- new cvs snapshot
  o port to qt4

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.0.2-7mdv2010.0
+ Revision: 433038
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.0.2-6mdv2009.0
+ Revision: 259974
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.0.2-5mdv2009.0
+ Revision: 247778
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.0.2-3mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import qmidiarp


* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.2-3mdv2007.0
- %%mkrel
- xdg menu
- fix x11 path

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.0.2-2mdk
- lib64 fix

* Mon Sep 20 2004 Austin Acton <austin@mandrake.org> 0.0.2-1mdk
- initial build
-
