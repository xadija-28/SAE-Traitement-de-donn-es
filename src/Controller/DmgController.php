<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class DmgController extends AbstractController
{
    #[Route('/dmg', name: 'app_dmg')]
    public function index(): Response
    {
        return $this->render('dmg/index.html.twig', [
            'controller_name' => 'DmgController',
        ]);
    }
    #[Route('/Blog', name: 'Blog')]
    public function Blog()
    {
        return $this->render('dmg/Blog.html.twig', [
            'controller_name' => 'DmgController',
        ]);
    }
}
