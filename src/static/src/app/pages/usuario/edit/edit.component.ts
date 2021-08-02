import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  value = null;  
  vehicleForm: FormGroup;

  constructor(private router: Router, private fb: FormBuilder) {   
    this.vehicleForm = new FormGroup({});
  }

  ngOnInit(): void {   
    this.initForm();
  }

  onGoToBackList(): void {
    ///this.navigationExtras.state.value = this.employee;
    this.router.navigate(['listV']);
  }

  onSave(): void {
    console.log('saved');
  }

  private initForm(){
    this.vehicleForm = this.fb.group({
      placa: ['', [Validators.required]],
      modelo: ['', [Validators.required]],
      capacidad: ['', [Validators.required]],
      kilometraje: ['', [Validators.required]],
      centro_operaciones_id: ['', [Validators.required]]
    })
  }

}
