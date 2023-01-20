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
    #[Route('/dmg/Cv', name: 'app_dmg_Cv')]
    public function CV(): Response
    {
        return $this->render('dmg/Cv.html.twig', [
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
}
