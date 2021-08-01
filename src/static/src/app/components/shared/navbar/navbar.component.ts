import { Component, OnInit, ViewChild } from '@angular/core';
import { MenuItem } from '../../../menu-item';
import { MatSidenav } from '@angular/material/sidenav';
import { BreakpointObserver } from '@angular/cdk/layout';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  
  @ViewChild(MatSidenav)
  sidenav!: MatSidenav;

  constructor(private observer: BreakpointObserver, private router:Router ) {}

  ngAfterViewInit() {
    // this.observer.observe(['(max-width: 800px)']).subscribe((res) => {
    //   if (res.matches) {
    //     this.sidenav.mode = 'over';
    //     this.sidenav.close();
    //   } else {
    //     this.sidenav.mode = 'side';
    //     this.sidenav.open();
    //   }
    // });

    // this.sidenav.mode = 'side';
    // this.sidenav.open();
  }


  menuItems: MenuItem[] = [
    {
      label: 'Sign In',
      icon: 'login',
      showOnMobile: false,
      showOnTablet: true,
      showOnDesktop: true
    },
    {
      label: 'Sign Up',
      icon: 'assignment',
      showOnMobile: true,
      showOnTablet: true,
      showOnDesktop: true
    },
    // {
    //   label: 'Pricing',
    //   icon: 'attach_money',
    //   showOnMobile: false,
    //   showOnTablet: false,
    //   showOnDesktop: true
    // },
    // {
    //   label: 'Docs',
    //   icon: 'notes',
    //   showOnMobile: false,
    //   showOnTablet: true,
    //   showOnDesktop: true
    // },
    // {
    //   label: 'Showcase',
    //   icon: 'slideshow',
    //   showOnMobile: false,
    //   showOnTablet: false,
    //   showOnDesktop: true
    // },
    // {
    //   label: 'Blog',
    //   icon: 'rss_feed',
    //   showOnMobile: false,
    //   showOnTablet: false,
    //   showOnDesktop: false
    // },
  ];  

  ngOnInit(): void {
  }

  RedirectHome(){
    this.router.navigate( ['/home'] )
  }

  RedirectLogin(){
    this.router.navigate( ['/login'] )
  }

  RedirectRegister(){
    this.router.navigate( ['/register'] )
  }
}
