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
    #[Route('/dmg/cv', name: 'app_dmg_cv')]
    public function Cv(): Response
    {
        return $this->render('dmg/cv.html.twig', [
            'controller_name' => 'DmgController',
        ]);
    }

    #[Route('/dmg/loisi', name: 'app_dmg_loisi')]
    public function loisi(): Response
    {
        return $this->render('dmg/loisi.html.twig', [
            'controller_name' => 'DmgController',
        ]);
    }
    #[Route('/dmg/portfolio', name: 'app_dmg_portfolio')]
    public function portfolio(): Response
    {
        return $this->render('dmg/portfolio.html.twig', [
            'controller_name' => 'DmgController',
        ]);
    }
    #[Route('/dmg/info', name: 'app_dmg_info')]
    public function info(): Response
    {
        return $this->render('dmg/info.html.twig', [
            'controller_name' => 'DmgController',
        ]);
    }
}
