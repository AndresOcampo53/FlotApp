import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss']
})
export class DetailsComponent implements OnInit {

  navigationExtras: NavigationExtras = {
    state: {
      value: null
    }
  }

  employee: any = null;  

  constructor(private router: Router) {    
    const navigation = this.router.getCurrentNavigation();
    this.employee = navigation?.extras?.state;

  }

  
  ngOnInit(): void {
  }
  
  onGoToEdit(): void {
    ///this.navigationExtras.state.value = this.employee;
    this.router.navigate(['editV', this.navigationExtras]);
  }

  onGoToBackList(): void {
    ///this.navigationExtras.state.value = this.employee;
    this.router.navigate(['listV']);
  }

  onDelete(): void {
    alert('Borrado');
  }

}
