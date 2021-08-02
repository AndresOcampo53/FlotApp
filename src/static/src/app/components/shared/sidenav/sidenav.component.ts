import { Component, OnInit, ViewChild } from '@angular/core';
import { BreakpointObserver } from '@angular/cdk/layout';
import { MatSidenav } from '@angular/material/sidenav';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-sidenav',
  templateUrl: './sidenav.component.html',
  styleUrls: ['./sidenav.component.scss']
})
export class SidenavComponent {
  @ViewChild(MatSidenav)
  sidenav!: MatSidenav;
  showmenu: boolean;

  constructor(private router:Router) {
    
    this.showmenu = true;
    
    const currentUrl = window.location.href; 
    this.router.events.subscribe((e) => {
      if (e instanceof NavigationEnd) {
        if(currentUrl.includes('/login')){
          this.showmenu = false;
        }
      }
    });
  }

  ngAfterViewInit() {
    // this.observer.observe(['(max-width: 800px)']).subscribe((res) => {
    //   if (!res.matches) {
    //     this.sidenav.mode = 'side';
    //     this.sidenav.close();
    //   } 
    //   else {
    //     this.sidenav.mode = 'side';
    //     this.sidenav.open();
    //   }
    // });

    this.sidenav.mode = 'side';
    this.sidenav.open();
  }

  RedirectHome(){
    this.router.navigate( ['/user'] )
  }

  RedirectUser(){
    this.router.navigate( ['/list'] )
  }

  RedirectVehicle(){
    this.router.navigate( ['/listV'] )
  }


  
}
