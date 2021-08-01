import { Component, OnInit } from '@angular/core';
import { NavigationExtras,Router } from '@angular/router';
import { Employee, EmployeeService } from 'src/app/services/employee.service';

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

  employee: Employee[] = [];  

  constructor(private router: Router, private _employeeService: EmployeeService) {    
   }  

  ngOnInit() {
    this.employee = this._employeeService.geEmployee();
    console.log(this.employee);    
  }
  
  onGoToEdit(item: any): void {
    //this.navigationExtras.state.value = item;
    this.router.navigate(['/edit', this.navigationExtras]);
  }

  onGoToDetails(item: any): void {    
    //this.navigationExtras.state.value = item;
    this.router.navigate(['details', this.navigationExtras]);
  }

  onGoToDelete(item: any): void { 
    
  }

  

 
}
