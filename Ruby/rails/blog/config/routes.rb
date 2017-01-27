Rails.application.routes.draw do
  #get 'posts/index'
  resources :posts
  #root 'posts#index' #place blog posts on root index 

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
