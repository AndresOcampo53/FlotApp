import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SharedComponent } from './components/shared/shared.component';
import { NavbarComponent } from './components/shared/navbar/navbar.component';
import { SidenavComponent } from './components/shared/sidenav/sidenav.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { UserComponent } from './components/user/user.component';
import { RegisterComponent } from './components/register/register.component';
import { HomeUserComponent } from "./components/user/home-user/home-user.component";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AngularMaterialModule } from './angular-material.module';
import { FlexLayoutModule } from "@angular/flex-layout";
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { PerfilComponent } from './components/user/perfil/perfil.component';
import { MatTableModule } from '@angular/material/table';
import { EmployeeService } from './services/employee.service';
@NgModule({
  declarations: [
    AppComponent,
    SharedComponent,
    NavbarComponent,
    SidenavComponent,
    HomeComponent,
    LoginComponent,
    UserComponent,
    RegisterComponent,
    HomeUserComponent,
    PerfilComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    AngularMaterialModule,
    FormsModule,    
    ReactiveFormsModule,
    FlexLayoutModule,
    HttpClientModule,
    MatSidenavModule,
    MatListModule,
    MatTableModule
    
  ],
  providers: [
    EmployeeService
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }
