import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  value = null;  
  employeeForm: FormGroup;

  constructor(private router: Router, private fb: FormBuilder) {   
    this.employeeForm = new FormGroup({});
  }

  ngOnInit(): void {   
    this.initForm();
  }

  onGoToBackList(): void {
    ///this.navigationExtras.state.value = this.employee;
    this.router.navigate(['list']);
  }

  onSave(): void {
    console.log('saved');
  }

  private initForm(){
    this.employeeForm = this.fb.group({
      nombre: ['', [Validators.required]],
      apellido: ['', [Validators.required]],
      cedula: ['', [Validators.required]],
      rol: ['', [Validators.required]]
    })
  }

}
