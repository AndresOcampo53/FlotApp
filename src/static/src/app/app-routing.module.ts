import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { HomeUserComponent } from './components/user/home-user/home-user.component';
import { PerfilComponent } from './components/user/perfil/perfil.component';
import { UserComponent } from './components/user/user.component';

const routes: Routes = [
  //{ path: 'home', component: HomeComponent},
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'user', component: UserComponent },
  { path: 'user-home', component: HomeUserComponent },
  { path: 'profile', component: PerfilComponent },
  { path: 'new', loadChildren: () => import('./pages/vehicle/new/new.module').then(m => m.NewModule) },
  { path: 'edit', loadChildren: () => import('./pages/vehicle/edit/edit.module').then(m => m.EditModule) },
  { path: 'details', loadChildren: () => import('./pages/vehicle/details/details.module').then(m => m.DetailsModule) },
  { path: 'list', loadChildren: () => import('./pages/vehicle/list/list.module').then(m => m.ListModule) },
  { path: '**',   redirectTo: 'login' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
