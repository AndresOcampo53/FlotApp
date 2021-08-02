import { Component, OnInit } from '@angular/core';
import { NavigationExtras, Router } from '@angular/router';
import { Vehicle, VehicleService } from 'src/app/services/vehicle.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  navigationExtras: NavigationExtras = {
    state: {
      value: null
    }
  }

  vehicle: Vehicle[] = [];  

  constructor(private router: Router, private _vehicleService: VehicleService) {    
   }  

  ngOnInit() {
    this.vehicle = this._vehicleService.geVehicle();    
  }
  
  onGoToEdit(item: any): void {
    //this.navigationExtras.state.value = item;
    this.router.navigate(['/editV', this.navigationExtras]);
  }

  onGoToDetails(item: any): void {    
    //this.navigationExtras.state.value = item;
    this.router.navigate(['detailsV', this.navigationExtras]);
  }

  onGoToDelete(item: any): void { 
    
  }
}
